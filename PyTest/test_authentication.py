import pytest, requests
from requests.auth import HTTPBasicAuth
from urllib.parse import urljoin
from IntegrationConfigManager import IntegrationConfigManager
import random, json, csv

@pytest.mark.authentication
@pytest.mark.compass
class TestAuthentication:

    @pytest.fixture
    def initial(self):
        # Load the config
        ccm = IntegrationConfigManager()
        config = ccm.load_config()
        
        # Load the environment data
        self.api_key = config["api_keys"][0]
        self.firmid = str(config["default_firmid"])
        self.host = config["service_url"]
        self.auth_url = config['auth_url']

    @pytest.fixture
    def initial_bad_api_key(self):
        # load the config
        ccm = IntegrationConfigManager()
        config = ccm.load_config()

        # load the environment data
        self.api_key = config["invalid_api_keys"][0]
        self.firmid = str(config["default_firmid"])
        self.host = config["service_url"]
        self.auth_url = config['auth_url']

    def load_ofa(self):
        # Load the user
        ccm = IntegrationConfigManager()
        default_user = ccm.load_user(
            firm_id=self.firmid, 
            user_type=['Administrator', 'OFA', 'RW User']
        )

        self.user = (default_user["username"], default_user["password"])
        
        # Set up compass to work with everything
        self.compass = requests.Session()
        self.compass.verify = False
        self.compass.auth = self.user
        self.compass.headers.update({
            "x-compass-firm-id": self.firmid,
            "x-compass-api-key": self.api_key,
            "Content-Type": "application/json"
        })
    
    def load_invalid_user(self):
        # Load the user
        ccm = IntegrationConfigManager()
        default_user = ccm.load_user(
            firm_id=self.firmid, 
            user_type=['Inactive']
        )

        self.user = (default_user["username"], default_user["password"])
        
        # Set up compass to work with everything
        self.compass = requests.Session()
        self.compass.verify = False
        self.compass.auth = self.user
        self.compass.headers.update({
            "x-compass-firm-id": self.firmid,
            "x-compass-api-key": self.api_key,
            "Content-Type": "application/json"
        })

    def load_bearer_token(self):
        ccm = IntegrationConfigManager()
        default_user = ccm.load_user(
            firm_id=self.firmid,
            user_type=['Administrator', 'OFA', 'RW User']
        )
        
        headers = {"accept": "application/json", "Content-Type": "application/json"}
        data = f'{{"firmid": {self.firmid}, "username": "{default_user["username"]}", "password": "{default_user["password"]}"}}'
        bearer_token = requests.post(self.auth_url, headers=headers, data=data, verify=False).json()['token']

        headers['x-compass-api-key'] = self.api_key
        headers['Authorization'] = f"Bearer {bearer_token}"

        self.compass = requests.Session()
        self.compass.headers = headers
        self.compass.verify = False
    
    def use_compass_user_token_only(self, compass_user_token, content_type = "application/json"):
        '''Function removes all of the headers except the user token and content type'''
        self.compass.auth = None
        self.compass.headers = {}
        self.compass.headers.update({'x-compass-token': compass_user_token, "Content-Type": content_type})

    @pytest.mark.dependency()
    @pytest.mark.smoke
    def test_good_credentials_with_basic_auth_returns_a_user_token(self, initial):
        '''Verifies a user can be authenticated with good credentials.'''
        self.load_ofa()
        r = self.compass.get(urljoin(self.host, '/api/user'))
        assert 'UserToken' in r.json()[0].keys()
        assert r.status_code == 200
    
    @pytest.mark.dependency()
    def test_a_bad_password_with_basic_auth_returns_401(self, initial):
        '''Verifies a bad password returns a 401'''
        self.load_ofa()
        # change the password for a known good user
        self.user = (self.user[0], 'lkjDFOIU23lkmsdf9878923')
        self.compass.auth = self.user
        # make the call, verify status code
        r = self.compass.get(urljoin(self.host, '/api/user'))
        assert r.status_code == 401

    @pytest.mark.dependency()
    @pytest.mark.smoke
    def test_password_is_case_sensitive(self, initial):
        '''Verifies the password is actually case sensitive'''
        self.load_ofa()
        # change the password for a known good user
        self.user = (self.user[0], self.user[1].upper())
        self.compass.auth = self.user
        # make the call, verify status code
        r = self.compass.get(urljoin(self.host, '/api/user'))
        assert r.status_code == 401
    
    @pytest.mark.dependency()
    @pytest.mark.failing
    def test_username_is_case_sensitive(self, initial):
        '''Verifies the username is actually case sensitive'''
        self.load_ofa()
        # change the username for a known good user
        self.user = (self.user[0].upper(), self.user[1])
        self.compass.auth = self.user
        # make the call, verify the status code
        r = self.compass.get(urljoin(self.host, '/api/user'))
        assert r.status_code == 401
    
    @pytest.mark.dependency()
    def test_revoked_api_key_gives_401(self, initial_bad_api_key):
        '''Verifies that if a revoked api key is given, the user receives a 401 unauthorized'''
        self.load_ofa()
        # change the api key
        r = self.compass.get(urljoin(self.host, '/api/user'))
        assert r.status_code == 401
    
    @pytest.mark.dependency()
    def test_inactive_user_receives_401(self, initial):
        '''Verifies that if an inactive user attempts to login, they receive a 401 error'''
        self.load_invalid_user()
        r = self.compass.get(urljoin(self.host, '/api/user'))
        assert r.status_code == 401
    
    @pytest.mark.dependency()
    @pytest.mark.smoke
    def test_a_user_can_get_a_compass_user_token_and_use_it_instead_of_basic_auth(self, initial):
        '''Verifies that a user can log in utilizing a token instead of basic authentication'''
        self.load_ofa()
        # Authenticate the user and get the token
        compass_user_token = self.compass.get(urljoin(self.host, '/api/user')).json()[0]['UserToken']
        # replace all of the headers
        self.use_compass_user_token_only(compass_user_token)
        # make calls to the various sections, verify a response.
        assert self.compass.get(urljoin(self.host, '/api/calllogs')).status_code == 200
        assert self.compass.get(urljoin(self.host, '/api/companies')).status_code == 200
        assert self.compass.get(urljoin(self.host, '/api/contacts')).status_code == 200
        assert self.compass.get(urljoin(self.host, '/api/leads')).status_code == 200
        assert self.compass.get(urljoin(self.host, '/api/opportunities')).status_code == 200
        assert self.compass.get(urljoin(self.host, '/api/personnel')).status_code == 200
        assert self.compass.get(urljoin(self.host, '/api/projects')).status_code == 200
    
    @pytest.mark.dependency()
    def test_a_user_with_a_compass_user_token_refreshes_token_with_call_to_api_user(self, initial):
        '''Verifies that a compass user token can be refreshed'''
        self.load_ofa()
        # Authenticate the user and get the token
        compass_user_token = self.compass.get(urljoin(self.host, '/api/user')).json()[0]['UserToken']
        self.use_compass_user_token_only(compass_user_token)
        # Make another authenticate call, verify we get the same token
        refreshed_user_token = self.compass.get(urljoin(self.host, '/api/user')).json()[0]['UserToken']
        assert compass_user_token == refreshed_user_token
    
    @pytest.mark.dependency()
    @pytest.mark.smoke
    def test_a_user_can_log_in_with_bearer_token(self, initial):
        '''Verifies a compass user can use bearer tokens'''
        # get credentials for a user we can use
        self.load_bearer_token()
        # make calls to the various sections, verify a response.
        assert self.compass.get(urljoin(self.host, '/api/calllogs')).status_code == 200
        assert self.compass.get(urljoin(self.host, '/api/companies')).status_code == 200
        assert self.compass.get(urljoin(self.host, '/api/contacts')).status_code == 200
        assert self.compass.get(urljoin(self.host, '/api/leads')).status_code == 200
        assert self.compass.get(urljoin(self.host, '/api/opportunities')).status_code == 200
        assert self.compass.get(urljoin(self.host, '/api/personnel')).status_code == 200
        assert self.compass.get(urljoin(self.host, '/api/projects')).status_code == 200
        