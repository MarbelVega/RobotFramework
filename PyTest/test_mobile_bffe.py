import pytest, requests
from requests.auth import HTTPBasicAuth
from urllib.parse import urljoin
from IntegrationConfigManager import IntegrationConfigManager

tests = [
    # TODO:  Here are the tests for the mobile bffe api.
    # Add a new row with marks in order to add a new endpoint, and all tests will execute.
    # Make sure to add the entity name to the ID's table below.
    pytest.param({"endpoint": "/api/contacts", "primary_key": "ContactId"}, marks=pytest.mark.contacts),
    pytest.param({"endpoint": "/api/companies", "primary_key": "CompanyId"}, marks=pytest.mark.companies),
]

# TODO:  If you add an entity above, please add the entity here so it outputs correctly
test_ids = ["CONTACTS", "COMPANIES"]

# NOTE:  You can tell you have added to the above correctly if you see your tests when you run
#   pytest --co   in this directory

class TestMobileBFFE:
    # Tests the mobile back end for front end stuff.

    @pytest.fixture(params=tests, ids=test_ids)
    def test_setup(self, request):
        # Load the config
        cm = IntegrationConfigManager()
        config = cm.load_config()
        self.host = config['mobile_bff_url']
        self.auth_url = config['auth_url']
        
        # Load users
        default_user = cm.load_user(
            user_type=['Administrator', 'OFA', 'RW User'],
            firm_id = f"{config['default_firmid']}"
        )
        self.firmid = default_user['firmid']
        self.username = default_user['username']
        self.password = default_user['password']

        # get a bearer token for use
        headers = {"accept": "application/json", "Content-Type": "application/json"}
        data = f'{{"firmid": {self.firmid}, "username": "{default_user["username"]}", "password": "{default_user["password"]}"}}'
        bearer_token = requests.post(self.auth_url, headers=headers, data=data, verify=False).json()['token']

        # Set up the mobile bffe api to work with everything
        self.api = requests.Session()
        self.api.verify = False
        self.api.headers.update({
            "Authorization": f"Bearer {bearer_token}",
            "accept": "application/json"
        })

        # parameters explicitly passed to tests
        self.endpoint = request.param['endpoint']
        #self.entity = request.param['test_entity']
        self.primary_key = request.param['primary_key']
    
    @pytest.mark.smoke
    @pytest.mark.mobile_bff
    def test_user_can_read_an_endpoint(self, test_setup):
        # Makes a simple get call to the endpoint, verifies a return
        r = self.api.get(f"{self.host}{self.endpoint}")
        assert self.primary_key in r.text
    
    @pytest.mark.smoke
    @pytest.mark.mobile_bff
    def test_an_endpoint_can_be_sized(self, test_setup):
        # Makes a get call to the endpoint specifying a number of records, verifies return size
        r = self.api.get(f"{self.host}{self.endpoint}?size=5")
        assert len(r.json()) == 5
    
    @pytest.mark.smoke
    @pytest.mark.mobile_bff
    def test_an_endpoint_can_be_paged(self, test_setup):
        # Makes a get call to the endpoint, then a second, and inspects the results
        #  checking that paging actually happens.
        r1 = self.api.get(f"{self.host}{self.endpoint}?size=12&from=0")
        r2 = self.api.get(f"{self.host}{self.endpoint}?size=12&from=50")
        all_items = zip(r1.json(), r2.json())
        assert len([(x,y) for x, y in all_items if x[self.primary_key] == y[self.primary_key]]) == 0
