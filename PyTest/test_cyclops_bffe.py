import pytest, requests
from requests.auth import HTTPBasicAuth
from urllib.parse import urljoin
from IntegrationConfigManager import IntegrationConfigManager

class CyclopsBFFEFixtures:
    # This class holds fixtures all of the test classes for cyclops use.

    @pytest.fixture
    def noauth_fixt(self):
        # Load the config
        cm = IntegrationConfigManager()
        config = cm.load_config()
        self.host = config['cyclops_bff_url']

    @pytest.fixture
    def normaluse_fixt(self):
        # Load the config
        cm = IntegrationConfigManager()
        config = cm.load_config()
        self.host = config['cyclops_bff_url']
        self.auth_url = config['auth_url']
        
        # Load users
        default_user = cm.load_user(
            user_type=['Administrator', 'OFA', 'RW User'],
            firm_id = f"{config['default_firmid']}"
        )
        self.firmid = default_user['firmid']
        
        headers = {"accept": "application/json", "Content-Type": "application/json"}
        data = f'{{"firmid": {self.firmid}, "username": "{default_user["username"]}", "password": "{default_user["password"]}"}}'
        bearer_token = requests.post(self.auth_url, headers=headers, data=data, verify=False).json()['token']
        
        # Set up the api to work with everything
        self.api = requests.Session()
        self.api.verify = False
        self.api.headers.update({
            "Authorization": f"Bearer {bearer_token}"
        })

@pytest.mark.cyclops_bff
class TestCyclopsBFFEGeneric(CyclopsBFFEFixtures):
    # Tests the cyclops back end for front end generic endpoints

    @pytest.mark.smoke
    def test_cfo_feature_can_be_requested_with_permissions(self, normaluse_fixt):
        # Make a request for a CFO Feature.  Assert a 204 status code.  (success)
        r = self.api.get(f"{self.host}/api/CFOFeature")
        assert r.status_code == 204
    
    @pytest.mark.smoke
    def test_cfo_feature_will_return_unauthorized_with_no_credentials(self, noauth_fixt):
        # Make a request for a CFO Feature.  Assert a 401 status code.
        r = requests.get(f"{self.host}/api/CFOFeature", verify=False)
        assert r.status_code == 401
    
    @pytest.mark.smoke
    def test_angular_typescript_can_be_returned_when_authenticated(self, normaluse_fixt):
        # Make a request for the angular typescript.  Assert that angular typescript was returned.
        r = self.api.get(f"{self.host}/api/client/typescript/angular")
        assert "export class" in r.text
    
    @pytest.mark.smoke
    def test_angular_typescript_can_be_returned_without_credentials(self, noauth_fixt):
        # Make a request for the angular typescript without credentials.  Assert that angular typescript was returned.
        r = requests.get(f"{self.host}/api/client/typescript/angular", verify=False)
        assert "export class" in r.text
    
    @pytest.mark.smoke
    def test_health_check_returns_healthy(self, normaluse_fixt):
        # Make a request to the health check endpoint.  Verify health check data was healty.
        r = self.api.get(f"{self.host}/Health")
        assert r.json()['status'] == 'Healthy'
    
    @pytest.mark.smoke
    def test_health_check_returns_healthy_when_not_using_credentials(self, noauth_fixt):
        # Make a request to the health check endpoint without credentials.  Verify health check data was healthy.
        r = requests.get(f"{self.host}/Health", verify=False)
        assert r.json()['status'] == 'Healthy'
    
@pytest.mark.cyclops_bff
@pytest.mark.call_logs
class TestCyclopsBFFECallLogForm(CyclopsBFFEFixtures):
    # Tests the cyclops back end for front end call log form items

    @pytest.fixture
    def blank_call_form_data(self):
        self.call_form_data = {
            "callers": [0],
            "attendees": { 
                "contactIds": [0],
                "personnelIds": [0]
                },
            "associations": {
                "contactIds": [0], 
                "opportunityIds": [0]
            }
        }

    @pytest.mark.smoke
    def test_blank_call_log_values_are_returned_when_no_data_is_Given(self, normaluse_fixt, blank_call_form_data):
        # Make a post call to return the blank call log data.  Assert we have been returned data.
        r = self.api.post(f"{self.host}/api/CallLogForm", json=self.call_form_data)
        assert len(r.json()['callers']) == 0
        assert len(r.json()['attendees']['contacts']) == 0
        assert len(r.json()['associations']['contacts']) == 0
        assert len(r.json()['associations']['opportunities']) == 0
        assert len(r.json()['associations']['companies']) == 0
    
    @pytest.mark.smoke
    def test_call_log_form_returns_call_dispositions(self, normaluse_fixt, blank_call_form_data):
        # Make a post call to the call log form.  Check the return contains call dispositions.
        r = self.api.post(f"{self.host}/api/CallLogForm", json=self.call_form_data)
        assert len(r.json()['callDispositions']) > 0
    
    @pytest.mark.smoke
    def test_call_log_form_returns_call_types(self, normaluse_fixt, blank_call_form_data):
        # Make a post call to the call log form.  Check the return contains call types.
        r = self.api.post(f"{self.host}/api/CallLogForm", json=self.call_form_data)
        assert len(r.json()['callTypes']) > 0
    
    @pytest.mark.smoke
    def test_call_log_form_returns_meeting_plan_status(self, normaluse_fixt, blank_call_form_data):
        # Turn the meeting plan on, verify the meeting plan return in the call log form.
        # Turn the meeting plan off, verify the meeting plan return in the call log form.
        # # Off State
        # # TODO:  Need to figure out how to turn this thing off...
        # r = self.api.post(urljoin(self.host, "/api/CallLogForm"), json=self.call_form_data)
        # assert r.json()['meetingPlanEnabled'] == False
        # On state
        r = self.api.post(f"{self.host}/api/CallLogForm", json=self.call_form_data)
        assert r.json()['meetingPlanEnabled'] == True

    @pytest.mark.smoke
    def test_i_can_search_the_notify_field_on_call_log_form(self, normaluse_fixt):
        # Make a request to search the notify field.  Verify the data returned.
        search_string = "rich" # TODO:  Vary this and the results.
        r = self.api.get(f"{self.host}/api/CallLogForm/search/notify?searchString={search_string}")
        assert len(r.json()['personnel']) > 0

    @pytest.mark.smoke
    @pytest.mark.failing
    def test_i_can_search_for_attendees_on_call_log_form(self, normaluse_fixt):
        search_string = "rich" # TODO:  Vary this and the results.
        r = self.api.get(f"{self.host}/api/CallLogForm/search/attendees?searchString={search_string}")
        assert len(r.json()['personnel']) > 0
        assert len(r.json()['contacts']) > 0

    @pytest.mark.smoke
    @pytest.mark.failing
    def test_i_can_search_for_associations_on_call_log_form(self, normaluse_fixt):
        search_string = "test" # TODO:  Maybe split this per section?  Needed.
        r = self.api.get(f"{self.host}/api/CallLogForm/search/associations?searchString={search_string}")
        assert len(r.json()['contacts']) > 0
        assert len(r.json()['projects']) > 0
        assert len(r.json()['leads']) > 0
        assert len(r.json()['opportunities']) > 0
        assert len(r.json()['companies']) > 0

@pytest.mark.cyclops_bff
@pytest.mark.opportunities
class TestCyclopsBFFEOpportunityCardView(CyclopsBFFEFixtures):
    # Tests the cyclops back end for front end opportunity card view items

    @pytest.fixture
    def empty_card_view_config(self):
        self.card_view_config = {
            "headerField": "",
            "displayAvgDays": False,
            "fields": "",
            "firmOrg": "",
            "maxDaysInStage": "0",
            "health": None,
            "autoAssociateNewOpps": None,
            "autoAssociateStaffRole": "46416",
            "stages": [
                11958, 11959, 11960, 11961, 11962, 11963, 11964, 11965, 11966, 11967, 11968, 11969,
                11970, 15874, 15875, 14495
            ],
        "scccEnabled": None,
        "enrichmentEnabled": None
        }

    # MARK A DEPENDENCY??
    @pytest.mark.smoke
    def test_i_can_get_the_opportunity_card_view_config(self, normaluse_fixt, empty_card_view_config):
        r = self.api.get(f"{self.host}/api/opportunitycardview/Config")
        assert r.json()['headerField'] == self.card_view_config['headerField']
    
    @pytest.mark.smoke
    def test_i_can_delete_the_opportunity_card_view_config(self, normaluse_fixt):
        r = self.api.delete(f"{self.host}/api/opportunitycardview/Config")
        assert r.status_code == 200  # possibility of false positive.  should make it more robust.

    @pytest.mark.smoke
    def test_i_can_create_an_opportunity_card_view_config_with_put(self, normaluse_fixt, empty_card_view_config):
        r = self.api.put(f"{self.host}/api/opportunitycardview/Config", json=self.card_view_config)
        assert r.status_code == 200  # will be false positives.  should break it out per field.
    
    @pytest.mark.smoke
    def test_i_can_update_an_opportunity_card_view_config_with_post(self, normaluse_fixt, empty_card_view_config):
        r = self.api.post(f"{self.host}/api/opportunitycardview/Config", json=self.card_view_config)
        assert r.status_code == 200 # will be false positives.  should break it out per field.
    
    @pytest.mark.smoke
    def test_i_can_get_company_firm_org_metadata(self, normaluse_fixt):
        # TODO:  Set the things and verify different settings
        r = self.api.get(f"{self.host}/api/opportunitycardview/FirmOrgs/CompaniesFirmOrgMetadata")
        assert r.json()['isDivisionsEnabled'] == True

    @pytest.mark.smoke
    def test_i_can_get_contact_firm_org_metadata(self, normaluse_fixt):
        # TODO:  Set the things and verify different settings
        r = self.api.get(f"{self.host}/api/opportunitycardview/FirmOrgs/ContactsFirmOrgMetadata")
        assert r.json()['isDivisionsEnabled'] == True
    
    @pytest.mark.smoke
    def test_i_can_get_opportunity_firm_org_metadata(self, normaluse_fixt):
        # TODO:  Set the things and verify different settings
        r = self.api.get(f"{self.host}/api/opportunitycardview/FirmOrgs/OpportunitiesFirmOrgMetadata")
        assert r.json()['isDivisionsEnabled'] == True
    
    @pytest.mark.smoke
    def test_i_can_get_lead_firm_org_metadata(self, normaluse_fixt):
        # TODO:  Set the things and verify different settings
        r = self.api.get(f"{self.host}/api/opportunitycardview/FirmOrgs/LeadsFirmOrgMetadata")
        assert r.json()['isDivisionsEnabled'] == True
    
    @pytest.mark.smoke
    def test_i_can_get_the_opportunity_card_view_summary(self, normaluse_fixt):
        # TODO:  Break down for each summary item
        r = self.api.get(f"{self.host}/api/opportunitycardview/Summary")
        assert r.json()['hasInactiveStages'] == True
    
    @pytest.mark.smoke
    def test_i_can_get_the_opportunity_card_view_state_from_couchbase(self, normaluse_fixt):
        r = self.api.get(f"{self.host}/api/opportunitycardview/State")
        assert r.json()['sort'] # TODO:  assertions for each section in line with the create/etc tests.
                                # This is only testing the field is there, so its technically valid...
    
    @pytest.mark.smoke
    def test_i_can_get_the_opportunity_card_view_sort_options(self, normaluse_fixt):
        # TODO:  Explore turning these off UI wise if thats possible... need to know reqs.
        r = self.api.get(f"{self.host}/api/opportunitycardview/SortOptions")
        assert len(r.json()) > 0

@pytest.mark.cyclops_bff
@pytest.mark.contacts
class TestCyclopsBFFEContactForm(CyclopsBFFEFixtures):
    # Tests the cyclops back end for front end contact form items

    @pytest.mark.smoke
    def test_i_can_get_contact_form_fields(self, normaluse_fixt):
        # TODO:  Break this apart to verify each field group
        search_string = "rlewis@cosential.com"
        r = self.api.get(f"{self.host}/api/ContactForm?emailAddress={search_string}")
        assert search_string in r.text
        assert len(r.json()["fieldGroups"]) > 1
    
    @pytest.mark.smoke
    @pytest.mark.failing
    def test_i_can_search_for_companies_on_contact_form(self, normaluse_fixt):
        # TODO:  Use compass to randomize this data
        search_string = "3100 Pearl"
        r = self.api.get(f"{self.host}/api/ContactForm/search/companies?searchString={search_string}")
        assert r.json()['companies'][0]['title'] == "3100 Pearl Street LLC"