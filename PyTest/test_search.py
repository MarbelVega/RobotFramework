import pytest, requests
from urllib.parse import urljoin
from IntegrationConfigManager import IntegrationConfigManager
import random, time
from faker import Faker
FAKER = Faker()
DELAY = 3  # It takes time for elastic search to pick up changes, so we wait x seconds on the tests...

tests = [
    pytest.param('api/projects', 'ProjectName', 'projects'),
    # pytest.param('api/contacts', 'FirstName', 'contacts'),
    # pytest.param('api/contacts', 'LastName', 'contacts'),
    # pytest.param('api/leads', 'Name', 'leads'),
    # pytest.param('api/opportunities', 'OpportunityName', 'opportunities'),
    # pytest.param('api/companies', 'Name', 'companies'),
    # pytest.param('api/personnel', 'FirstName', 'personnel'),
    # pytest.param('api/personnel', 'LastName', 'personnel')
]
@pytest.mark.searchservice
@pytest.mark.parametrize('route,search_field,web_param', tests)
class TestCompassSearch:
    def setmeup(self, route):
        ccm = IntegrationConfigManager()
        config = ccm.load_config()

        self.api_key = config['api_keys'][0]
        self.firmid = str(config['default_firmid'])
        self.host = config['service_url']

        self.web_url = config['web_url']

        default_user = ccm.load_user(
            firm_id = self.firmid,
            user_type = ["Administrator", "OFA", "RW User"]
        )
        self.user = (default_user['username'], default_user['password'])

        self.web = requests.Session()
        self.web.verify = False
        # login
        self.web.post(f'{self.web_url}/index.cfm', data = {'username': default_user['username'], 'password': default_user['password'], 'firmid': self.firmid}, verify=False)

        self.compass = requests.Session()
        self.compass.verify = False
        self.compass.auth = self.user
        self.compass.headers.update({
            'x-compass-firm-id': self.firmid,
            'x-compass-api-key': self.api_key,
            'Content-Type': 'application/json'
        })

    def get_searchable_records(self, route):
        r = self.compass.get(f'{self.host}/{route}', verify=False)
        self.current_records = r.json()
    
    def get_route_schema(self, route):
        schema = self.compass.get(f'{self.host}/{route}/schema', verify=False).json()
        return schema
    
    def get_primary_key(self, route):
        schema = self.get_route_schema(route)
        self.current_primary_key = [prop['PropertyName'] for prop in schema if prop['IsPrimaryKey']][0]
    
    def make_fake_data(self, route, search_field):
        if "FirstName" not in search_field and "LastName" not in search_field:
            data = {f"{search_field}": FAKER.md5()}
        else:
            data = {"FirstName": FAKER.md5(), "LastName": FAKER.md5()}
        # special association requirements for opportunities or contacts
        if "opportunities" or "contacts" in route:
            company = random.choice(self.compass.get(f"{self.host}/api/companies", verify=False).json())['CompanyId']
            if "opportunities" in route:
                data['ClientId'] = company
            else:
                data['CompanyId'] = company
        return data

    @pytest.mark.compass
    def test_field_is_searchable_in_compass_schema(self, route, search_field, web_param):
        self.setmeup(route)
        properties = self.get_route_schema(route)
        for prop in properties:
            if prop['PropertyName'] == search_field:
                assert prop['Searchable'] == True

    @pytest.mark.compass
    def test_existing_records_can_be_searched_in_compass_by_field(self, route, search_field, web_param):
        # Search by a field with text
        self.setmeup(route)
        self.get_searchable_records(route)
        single = random.choice(self.current_records)
        text = single[search_field]
        r = self.compass.get(f'{self.host}/{route}/search?q={search_field}:{text}', verify=False)
        assert str(text) in r.text

    @pytest.mark.compass
    def test_existing_records_can_be_searched_in_compass_no_field_specified(self, route, search_field, web_param):
        self.setmeup(route)
        self.get_searchable_records(route)
        single = random.choice(self.current_records)
        text = single[search_field]
        r = self.compass.get(f'{self.host}/{route}/search?q={text}', verify=False)
        assert str(text) in r.text

    @pytest.mark.compass
    def test_new_record_can_be_searched_in_compass(self, route, search_field, web_param):
        self.setmeup(route)
        data = self.make_fake_data(route, search_field)
        r = self.compass.post(f'{self.host}/{route}', data=str([data]), verify=False)
        text = r.json()[0][search_field]
        time.sleep(DELAY)
        r = self.compass.get(f'{self.host}/{route}/search?q={text}', verify=False)
        assert str(text) in r.text

    @pytest.mark.compass
    def test_updated_record_can_be_searched_in_compass(self, route, search_field, web_param):
        self.setmeup(route)
        self.get_searchable_records(route)
        self.get_primary_key(route)
        single = random.choice(self.current_records)
        data = self.make_fake_data(route, search_field)
        record_id = single[self.current_primary_key]
        r = self.compass.put(f'{self.host}/{route}/{record_id}', data=str(data), verify=False)
        if "contacts" in route:
            text = r.json()[0][search_field]
        else:
            text = r.json()[search_field]
        time.sleep(DELAY)
        r = self.compass.get(f'{self.host}/{route}/search?q={text}', verify=False)
        assert str(text) in r.text

    @pytest.mark.compass
    def test_deleted_records_can_be_searched_in_compass(self, route, search_field, web_param):
        if 'leads' in route:
            pytest.skip(f"{route} marked as skipped due to being broken in old search bug.")
        self.setmeup(route)
        self.get_searchable_records(route)
        self.get_primary_key(route)
        single = random.choice(self.current_records)
        record_id = single[self.current_primary_key]
        text=single[search_field]
        r = self.compass.delete(f'{self.host}/{route}/{record_id}', verify=False)
        time.sleep(DELAY)
        r = self.compass.get(f'{self.host}/{route}/search?q={text}&includeDeleted=true', verify=False)
        assert str(text) in r.text

    @pytest.mark.quicksearch
    def test_existing_records_in_quicksearch_can_be_searched(self, route, search_field, web_param):
        self.setmeup(route)
        self.get_searchable_records(route)
        text = self.current_records[0][search_field]
        r = self.web.get(f"{self.web_url}/com/util/quicksearch.cfc?method={web_param}&q={text}", verify=False)
        assert str(text) in r.text

    @pytest.mark.quicksearch
    def test_new_records_in_quicksearch_can_be_searched(self, route, search_field, web_param):
        self.setmeup(route)
        data = self.make_fake_data(route, search_field)
        r = self.compass.post(f"{self.host}/{route}", data=str([data]))
        time.sleep(DELAY)
        text = r.json()[0][search_field]
        r = self.web.get(f"{self.web_url}/com/util/quicksearch.cfc?method={web_param}&q={text}", verify=False)
        assert str(text) in r.text

    @pytest.mark.quicksearch
    def test_updated_records_in_quicksearch_can_be_searched(self, route, search_field, web_param):
        self.setmeup(route)
        self.get_searchable_records(route)
        self.get_primary_key(route)
        single = random.choice(self.current_records)
        data = self.make_fake_data(route, search_field)
        record_id = single[self.current_primary_key]
        r = self.compass.put(f'{self.host}/{route}/{record_id}', data=str(data), verify=False)
        text = data[search_field]
        time.sleep(DELAY)
        r = self.web.get(f"{self.web_url}/com/util/quicksearch.cfc?method={web_param}&q={text}", verify=False)
        assert str(text) in r.text
