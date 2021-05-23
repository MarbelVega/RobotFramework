import pytest, requests
from requests.auth import HTTPBasicAuth
from urllib.parse import urljoin
from IntegrationConfigManager import IntegrationConfigManager
import random, json, csv

tests = [
    # A note here.  We could move these to CSV, but then we would lose the ability to use marks.

    ## Call Log Tests #############################################################################
    # pytest.param('api/calllogs','calldisposition','id','id', marks=[pytest.mark.calllogs, pytest.mark.calldispositions, pytest.mark.calls]),
    # pytest.param('api/calllogs','calltype','id','id', marks=[pytest.mark.calllogs, pytest.mark.calltypes, pytest.mark.calls]),

    ## Company Tests ##############################################################################
    # pytest.param('api/companies','companytypes','CompanyId','CompanyTypeID',marks=[pytest.mark.companies, pytest.mark.companytypes]),
    # pytest.param('api/companies','sdbt','CompanyId','Id',marks=[pytest.mark.companies, pytest.mark.sdbt]),
    # pytest.param('api/companies','naics','CompanyId','Id',marks=[pytest.mark.companies, pytest.mark.naics]),
    # pytest.param('api/companies','sic','CompanyId','Id',marks=[pytest.mark.companies, pytest.mark.sic]),
    # pytest.param('api/companies','primarycategories','CompanyId','PrimaryCategoryId',marks=[pytest.mark.companies, pytest.mark.primarycategories]),
    # pytest.param('api/companies','legalstructure','CompanyId','LSOID',marks=[pytest.mark.companies, pytest.mark.legalstructure]),
    # pytest.param('api/companies','offices','CompanyId','OfficeID',marks=[pytest.mark.companies, pytest.mark.offices]),
    # pytest.param('api/companies','territories','CompanyId','TerritoryID',marks=[pytest.mark.companies, pytest.mark.territories]),
    # pytest.param('api/companies','practiceareas','CompanyId','PracticeAreaId',marks=[pytest.mark.companies, pytest.mark.practiceareas]),
    # pytest.param('api/companies','studios','CompanyId','StudioId',marks=[pytest.mark.companies, pytest.mark.studios]),
    # pytest.param('api/companies','divisions','CompanyId','DivisionID',marks=[pytest.mark.companies, pytest.mark.divisions]),

    ## Contact Tests ###############################################################################
    # pytest.param('api/contacts','contact_category','ContactId','ContactCategoryID',marks=[pytest.mark.contacts, pytest.mark.contactcategory]),
    # pytest.param('api/contacts','advmaillists','ContactId','AdvMailListID',marks=[pytest.mark.contacts, pytest.mark.advancedmaillists]),
    # pytest.param('api/contacts','contact_mailinglist','ContactId','MailingListID',marks=[pytest.mark.contacts, pytest.mark.maillists]),
    # pytest.param('api/contacts','contact_contacttypes','ContactId','ContactTypeID',marks=[pytest.mark.contacts, pytest.mark.contacttypes]),
    # pytest.param('api/contacts','influencelevel','ContactId','Id',marks=[pytest.mark.contacts, pytest.mark.influencelevel]),
    # pytest.param('api/contacts','offices','ContactId','OfficeID',marks=[pytest.mark.contacts, pytest.mark.offices]),
    # pytest.param('api/contacts','territories','ContactId','TerritoryID',marks=[pytest.mark.contacts, pytest.mark.territories]),
    # pytest.param('api/contacts','practiceareas','ContactId','PracticeAreaId',marks=[pytest.mark.contacts, pytest.mark.practiceareas]),
    # pytest.param('api/contacts','studios','ContactId','StudioId',marks=[pytest.mark.contacts, pytest.mark.studios]),
    # pytest.param('api/contacts','divisions','ContactId','DivisionID',marks=[pytest.mark.contacts, pytest.mark.divisions]),
    
    ## Lead Tests ##################################################################################
    # pytest.param('api/leads','contracttypes','LeadId','Id',marks=[pytest.mark.leads, pytest.mark.contracttypes]),
    # pytest.param('api/leads','primarycategories','LeadId','PrimaryCategoryId',marks=[pytest.mark.leads, pytest.mark.primarycategories]),
    # pytest.param('api/leads','riskprofile','LeadId','Id',marks=[pytest.mark.leads, pytest.mark.riskprofile]),
    # pytest.param('api/leads','leadtypes','LeadId','Id',marks=[pytest.mark.leads, pytest.mark.leadtypes]),
    # pytest.param('api/leads','score','LeadId','Id',marks=[pytest.mark.leads, pytest.mark.score]),
    # pytest.param('api/leads','secondarycategories','LeadId','SecondaryCategoryID',marks=[pytest.mark.leads, pytest.mark.secondarycategories]),
    # pytest.param('api/leads','servicetypes','LeadId','ServiceTypeId',marks=[pytest.mark.leads, pytest.mark.servicetypes]),
    # pytest.param('api/leads','source','LeadId','Id',marks=[pytest.mark.leads, pytest.mark.source]),
    # pytest.param('api/leads','recordsource','LeadId','Id',marks=[pytest.mark.leads, pytest.mark.recordsource]),
    # pytest.param('api/leads','offices','LeadId','OfficeID',marks=[pytest.mark.leads, pytest.mark.offices]),
    # pytest.param('api/leads','territories','LeadId','TerritoryID',marks=[pytest.mark.leads, pytest.mark.territories]),
    # pytest.param('api/leads','practiceareas','LeadId','PracticeAreaId',marks=[pytest.mark.leads, pytest.mark.practiceareas]),
    # pytest.param('api/leads','studios','LeadId','StudioId',marks=[pytest.mark.leads, pytest.mark.studios]),
    # pytest.param('api/leads','divisions','LeadId','DivisionID',marks=[pytest.mark.leads, pytest.mark.divisions]),

    ## Opportunity Tests ###########################################################################
    pytest.param('api/opportunities','primarycategories','OpportunityId','PrimaryCategoryId',marks=[pytest.mark.opportunities, pytest.mark.primarycategories, pytest.mark.primary_categories]),
    pytest.param('api/opportunities','secondarycategories','OpportunityId','SecondaryCategoryID',marks=[pytest.mark.opportunities, pytest.mark.secondarycategories]),
    pytest.param('api/opportunities','servicetypes','OpportunityId','ServiceTypeId',marks=[pytest.mark.opportunities, pytest.mark.servicetypes]),
    pytest.param('api/opportunities','deliverymethod','OpportunityId','DeliveryMethodID',marks=[pytest.mark.opportunities, pytest.mark.deliverymethod]),
    pytest.param('api/opportunities','clienttypes','OpportunityId','Id',marks=[pytest.mark.opportunities, pytest.mark.clienttypes, pytest.mark.client_types]),
    pytest.param('api/opportunities','offices','OpportunityId','OfficeID',marks=[pytest.mark.opportunities, pytest.mark.offices]),
    pytest.param('api/opportunities','territories','OpportunityId','TerritoryID',marks=[pytest.mark.opportunities, pytest.mark.territories]),
    pytest.param('api/opportunities','practiceareas','OpportunityId','PracticeAreaId',marks=[pytest.mark.opportunities, pytest.mark.practiceareas]),
    pytest.param('api/opportunities','studios','OpportunityId','StudioId',marks=[pytest.mark.opportunities, pytest.mark.studios]),
    pytest.param('api/opportunities','divisions','OpportunityId','DivisionID',marks=[pytest.mark.opportunities, pytest.mark.divisions]),

    ## Personnel Tests #############################################################################
    # pytest.param('api/personnel','contractorcategories','PersonnelId','Id',marks=[pytest.mark.personnel, pytest.mark.contractorcategories]),
    # pytest.param('api/personnel','offices','PersonnelId','OfficeID',marks=[pytest.mark.personnel, pytest.mark.offices]),
    # pytest.param('api/personnel','territories','PersonnelId','TerritoryID',marks=[pytest.mark.personnel, pytest.mark.territories]),
    # pytest.param('api/personnel','practiceareas','PersonnelId','PracticeAreaId',marks=[pytest.mark.personnel, pytest.mark.practiceareas]),
    # pytest.param('api/personnel','studios','PersonnelId','StudioId',marks=[pytest.mark.personnel, pytest.mark.studios]),
    # pytest.param('api/personnel','divisions','PersonnelId','DivisionID',marks=[pytest.mark.personnel, pytest.mark.divisions]),
    
    ## Project Tests ###############################################################################
    # pytest.param('api/projects','constructiontype','ProjectId','Id',marks=[pytest.mark.projects, pytest.mark.constructiontype]),
    # pytest.param('api/projects','secondarycategories','ProjectId','SecondaryCategoryID',marks=[pytest.mark.projects, pytest.mark.secondarycategories]),
    # pytest.param('api/projects','projectrank','ProjectId','Id',marks=[pytest.mark.projects, pytest.mark.projectrank]),
    # pytest.param('api/projects','publishablereason','ProjectId','Id',marks=[pytest.mark.projects, pytest.mark.publishablereason]),
    # pytest.param('api/projects','deliverymethod','ProjectId','Id',marks=[pytest.mark.projects, pytest.mark.deliverymethod]),
    # pytest.param('api/projects','sf330profilecode','ProjectId','ProfileCodeId',marks=[pytest.mark.projects, pytest.mark.sf330profilecode]),
    # pytest.param('api/projects','sf254profilecode','ProjectId','ProfileCodeId',marks=[pytest.mark.projects, pytest.mark.sf254profilecode]),
    # pytest.param('api/projects','primarycategories','ProjectId','PrimaryCategoryId',marks=[pytest.mark.projects, pytest.mark.primarycategories, pytest.mark.primary_categories]),
    # pytest.param('api/projects','offices','ProjectId','OfficeID',marks=[pytest.mark.projects, pytest.mark.offices]),
    # pytest.param('api/projects','territories','ProjectId','TerritoryID',marks=[pytest.mark.projects, pytest.mark.territories]),
    # pytest.param('api/projects','practiceareas','ProjectId','PracticeAreaId',marks=[pytest.mark.projects, pytest.mark.practiceareas]),
    # pytest.param('api/projects','studios','ProjectId','StudioId',marks=[pytest.mark.projects, pytest.mark.studios]),
    # pytest.param('api/projects','divisions','ProjectId','DivisionID',marks=[pytest.mark.projects, pytest.mark.divisions]),
]

def pathify(host, ordered_parts_aray_all_strings_no_slashes):
    """ This function takes an ordered array with no slashes, and returns a URL.
        Example use would be sending it something like ['api/projects', '83523', 'primarycategories', '823512']
            as the array, and something as the host such as https://api.company.com/.
        In this situation, we can expect the return to look like this:
        https://api.company.com/api/projects/83523/primarycategories/823512
    """
    return urljoin(host, '/'.join(ordered_parts_aray_all_strings_no_slashes))

@pytest.mark.associations
@pytest.mark.compass
@pytest.mark.parametrize('parent_route,child_route,parent_primary_key,child_primary_key', tests)
class TestGenericAssociations:

    # Here we have a setup function.  Due to the way pytest works, we have to call this ourselves on every tests when
    #   parametrizing the entire class.
    def setmeup(self, parent, parent_primary_key):
        # Load the config
        ccm = IntegrationConfigManager()
        config = ccm.load_config()
        
        # Load the environment data
        self.api_key = config["api_keys"][0]
        self.firmid = str(config["default_firmid"])
        self.host = config["service_url"]

        # Load the user
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

        # We need to get some record ID's to work with this stuff.
        record_url = pathify(self.host, [parent])
        request = self.compass.get(record_url)
        self.this_record_id = request.json()[0][parent_primary_key]

    @pytest.mark.dependency()
    def test_association_can_be_single_posted(self, parent_route, child_route, parent_primary_key, child_primary_key):
        # Post a single association.  Verify the association happened.

        # Set up the test
        self.setmeup(parent_route, parent_primary_key)

        # Query the management URL for all of the records we could use to associate
        management_url = pathify(self.host, [parent_route, child_route])
        records = self.compass.get(management_url).json()

        # build the association URL and the association data
        association_url = pathify(self.host, [parent_route, str(self.this_record_id), child_route])
        record_for_test = random.choice(records)[child_primary_key]
        body = [{str(child_primary_key): record_for_test}]
        r = self.compass.post(association_url, data=str(body))
        assert str(record_for_test) in r.text

    @pytest.mark.dependency()
    def test_single_association_can_be_viewed(self, parent_route, child_route, parent_primary_key, child_primary_key):
        # Read a single association from a record, and verifies it can be read.
        # Set up the test
        self.setmeup(parent_route, parent_primary_key)

        if child_route in ['sdbt', 'legalstructure', 'naics', 'sic', 'sf330profilecode', 'sf254profilecode']:
            pytest.skip(f"The {child_route} endpoint does not support this action.")

        # Grab a single record that should already be on the record for viewing
        association_url = pathify(self.host, [parent_route, str(self.this_record_id), child_route])
        associated_id = self.compass.get(association_url).json()[0][child_primary_key]

        # Query the single record, verify the response
        associated_record_url = pathify(self.host, [parent_route, str(self.this_record_id), child_route, str(associated_id)])
        request = self.compass.get(associated_record_url)
        assert str(associated_id) in request.text

    @pytest.mark.dependency()
    def test_single_association_can_be_removed(self, parent_route, child_route, parent_primary_key, child_primary_key):
        # Remove a single association from a record, and verifies it is gone.
        # Set up the test
        self.setmeup(parent_route, parent_primary_key)

        # Grab a single record that should be already on the record for deleting
        association_url = pathify(self.host, [parent_route, str(self.this_record_id), child_route])
        associated_id = self.compass.get(association_url).json()[0][child_primary_key]

        # Remove the single record, verify the response
        associated_record_url = pathify(self.host, [parent_route, str(self.this_record_id), child_route, str(associated_id)])
        request = self.compass.delete(associated_record_url)
        request = self.compass.get(association_url)
        assert str(associated_id) not in request.text

    @pytest.mark.dependency()
    def test_all_associations_can_be_removed(self, parent_route, child_route, parent_primary_key, child_primary_key):
        # Remove all of the associations from the endpoint, then verifies there are none.

        # TODO:  MAY BE NONSTANDARD :TODO #
        # Set up the test
        self.setmeup(parent_route, parent_primary_key)

        # Send a delete to the association url, verify results.
        association_url = pathify(self.host, [parent_route, str(self.this_record_id), child_route])
        request = self.compass.delete(association_url)
        request = self.compass.get(association_url)
        # sometimes on empty items, we return the word null.  This is to catch those.
        if request.json().__class__ == list:
            assert len(request.json()) == 0
        else:
            assert request.text == 'null'