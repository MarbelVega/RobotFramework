import pytest, requests
from requests.auth import HTTPBasicAuth
from urllib.parse import urljoin
from IntegrationConfigManager import IntegrationConfigManager
from faker import Faker

# for random data
FAKER = Faker()

tests = [
    # These are the endpoints that follow this pattern.
    # We include the record type first in big letters, so that way we can easily
    #   distinguish it durning run.
    # We've also marked each line so that we can run it with just it's mark.
    pytest.param('CONTACT APP METADATA ENDPOINT', '/api/contacts', 'ContactId', marks=pytest.mark.contacts),
    pytest.param('PROJECT APP METADATA ENDPOINT', '/api/projects', 'ProjectId', marks=pytest.mark.projects),
    pytest.param('OPPORTUNITY APP METADATA ENDPOINT', '/api/opportunities', 'OpportunityId', marks=pytest.mark.opportunities),
    pytest.param('LEAD APP METADATA ENDPOINT', '/api/leads', 'LeadId', marks=pytest.mark.leads),
    pytest.param('PERSONNEL APP METADATA ENDPOINT', '/api/personnel', 'PersonnelId', marks=pytest.mark.personnel),
    pytest.param('COMPANY APP METADATA ENDPOINT', '/api/companies', 'CompanyId', marks=pytest.mark.companies)
]

@pytest.mark.compass
@pytest.mark.metadata
@pytest.mark.app
@pytest.mark.parametrize('record_type,endpoint,record_id_field', tests)
class TestRecordAppMetadata:

    # Here we have a setup function.  Due to the way pytest works, we have to call this ourselves on every tests when
    #   parametrizing the entire class.
    def setmeup(self, record_type, endpoint, record_id_field):
        # Load the config
        ccm = IntegrationConfigManager()
        config = ccm.load_config()
        
        # Load the environment data
        self.api_key_1 = config["api_keys"][0]
        self.api_key_2 = config["api_keys"][1]
        self.firmid = str(config["default_firmid"])
        self.host = config["service_url"]

        # Load users
        default_user = ccm.load_user(
            firm_id=self.firmid, 
            user_type=['Administrator', 'OFA', 'RW User']
        )
        other_user = ccm.load_user(
            firm_id=self.firmid, 
            user_type=['Administrator', 'OFA', 'RW User'], 
            exclude_users=[default_user['username']]
        )

        self.username_1 = default_user["username"]
        self.password_1 = default_user["password"]
        self.username_2 = other_user["username"]
        self.password_2 = other_user["password"]
        
        # Set up LOREM
        self.post_data = FAKER.paragraph(nb_sentences=5, variable_nb_sentences=True)
        self.put_data = FAKER.paragraph(nb_sentences=5, variable_nb_sentences=True)

        # Credential Tuples to make fast user switching possible later
        self.user_1 = (self.username_1, self.password_1)
        self.user_2 = (self.username_2, self.password_2)

        # Set up compass to work with everything
        self.compass = requests.Session()
        self.compass.verify = False
        self.compass.auth = self.user_1
        self.compass.headers.update({
            "x-compass-firm-id": self.firmid,
            "x-compass-api-key": self.api_key_1
        })

        # We need to get some record ID's to work with this stuff.
        request = self.compass.get(urljoin(self.host, endpoint))

        self.record_1 = request.json()[0][record_id_field]
        self.record_2 = request.json()[1][record_id_field]

        # Set up the metadata endpoints to make writing the tests easier.  Get them here!
        self.record_1_metadata = f"{endpoint}/{self.record_1}/metadata/app"
        self.record_2_metadata = f"{endpoint}/{self.record_2}/metadata/app"
    

    @pytest.mark.dependency()
    def test_record_app_metadata_returns_no_data_on_post(self, record_type, endpoint, record_id_field):
        # We post some metadata to the app endpoint, and we make sure there is no return.
        self.setmeup(record_type,endpoint,record_id_field)
        r = self.compass.post(urljoin(self.host, self.record_2_metadata), json=self.post_data)
        assert r.text == ''
    
    @pytest.mark.dependency()
    def test_record_app_metadata_returns_no_data_on_put(self, record_type, endpoint, record_id_field):
        # We put some metadata to the app endpoint, and we make sure there is no return.
        self.setmeup(record_type,endpoint,record_id_field)
        r = self.compass.put(urljoin(self.host, self.record_2_metadata), json=self.put_data)
        assert r.text == ''
    
    @pytest.mark.dependency()
    def test_record_app_metadata_returns_no_data_on_delete(self, record_type, endpoint, record_id_field):
        # We delete some metadata to the app endpoint, and we expect there is no return.
        self.setmeup(record_type,endpoint,record_id_field)
        r = self.compass.delete(urljoin(self.host, self.record_2_metadata))
        assert r.text == ''

    @pytest.mark.dependency(name='APPREADBACKPOST')
    def test_record_app_metadata_can_be_read_back_when_posted(self, record_type, endpoint, record_id_field):
        # We should be able to reread the metadata we've just posted in the app section
        #   of the metadata.
        self.setmeup(record_type,endpoint,record_id_field)
        r = self.compass.post(urljoin(self.host, self.record_1_metadata), json=self.post_data)
        r = self.compass.get(urljoin(self.host, self.record_1_metadata))
        assert self.post_data in r.text
    
    @pytest.mark.dependency(depends=["APPREADBACKPOST"])
    def test_record_app_metadata_can_not_be_read_from_second_api_key(self, record_type, endpoint, record_id_field):
        # We should not be able to read the metadata we've just posted when we use a
        #   second api key, since the metadata is "locked" to the original api key.
        self.setmeup(record_type,endpoint,record_id_field)
        r = self.compass.post(urljoin(self.host, self.record_1_metadata), json=self.post_data)
        # Switching out the API Key, then making our request
        self.compass.headers.update({"x-compass-api-key": self.api_key_2})
        r = self.compass.get(urljoin(self.host, self.record_1_metadata))
        # Make sure we reset the data we've changed before we assert
        self.compass.headers.update({"x-compass-api-key": self.api_key_1})
        # We want to verify that this actually succeeded, so cut out the false positive that would
        #   occur when we failed to authenticate.
        assert self.post_data not in r.text
    
    @pytest.mark.dependency(name='APPREADBACKPOST2USER', depends=["APPREADBACKPOST"])
    def test_record_app_metadata_can_be_read_from_second_user(self, record_type, endpoint, record_id_field):
        # We should be able to read the metadata we've just posted when we use a
        #   second user.  This is because the metadata is "locked" to the api key.
        self.setmeup(record_type,endpoint,record_id_field)
        r = self.compass.post(urljoin(self.host, self.record_1_metadata), json=self.post_data)
        # Switching out the user, then making the request.
        self.compass.auth = self.user_2
        r = self.compass.get(urljoin(self.host, self.record_1_metadata))
        print(r.text)
        # Resetting our user before we verify.
        self.compass.auth = self.user_1
        assert self.post_data in r.text
    
    @pytest.mark.dependency()
    def test_record_app_metadata_can_be_read_back_when_putted(self, record_type, endpoint, record_id_field):
        # We should be able to reread the metadata we've just putted in the app section
        #   of the metadata.
        self.setmeup(record_type,endpoint,record_id_field)
        r = self.compass.put(urljoin(self.host, self.record_1_metadata), json=self.put_data)
        r = self.compass.get(urljoin(self.host, self.record_1_metadata))
        assert self.put_data in r.text

    @pytest.mark.dependency(depends=["DELETEAPPDATA"])
    def test_record_app_metadata_can_be_read_even_when_deleted(self, record_type, endpoint, record_id_field):
        # We send a get request to a record's app metadata endpoint when we know it is
        #   deleted, and verify we get our expected return.
        self.setmeup(record_type,endpoint,record_id_field)
        r = self.compass.delete(urljoin(self.host, self.record_1_metadata))
        r = self.compass.get(urljoin(self.host, self.record_1_metadata))
        assert (r.text == 'null' or r.text == "")
