from urllib.parse import urljoin

import json
import pytest
import requests
from IntegrationConfigManager import IntegrationConfigManager


@pytest.mark.compass
class TestAddressSharing:

    @pytest.fixture
    def setup(self, request):
        # Load the config
        ccm = IntegrationConfigManager()
        config = ccm.load_config()
        
        # Load the environment data
        self.api_key = config["api_keys"][0]
        self.firmid = str(config["default_firmid"])
        self.host = config["service_url"]
        print(self.host)

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
        return request

    @pytest.mark.dependency()
    def test_contact_gets_address_from_company(self, setup):

        #create a company
        self.companiesUrl = urljoin(self.host, '/api/companies')
        body = [json.load(open('Compass/payloads/companies.json', 'r'))]
        response = self.compass.post(self.companiesUrl, json=body)
        assert type(response.json()[0]['CompanyId']) is int
        companyId = response.json()[0]['CompanyId']
        setup.config.cache.set('company_id', companyId)
        print("Created company with id - ", companyId)

       #add address to the created company
        global companyAddressesUrl
        companyAddressesUrl = urljoin(self.host, '/api/companies/'+ f'{companyId}' + '/addresses')
        body = [json.load(open('Compass/payloads/addresses.json', 'r'))]
        city = body[0]['City']
        zip = body[0]['PostalCode']
        country = body[0]['CountryName']
        phone = body[0]['OfficePhone']
        response = self.compass.post(companyAddressesUrl, json= body)
        assert response.status_code == 200, "CREATE COMPANY ADDRESS FAILED"
        addressId = response.json()[0]['AddressID']        # default address
        setup.config.cache.set('address_id', addressId)

        #create contact linked to same company and verify address is carried over
        contactsUrl = urljoin(self.host, '/api/contacts')
        body = [json.load(open('Compass/payloads/contacts.json', 'r'))]
        body[0]['CompanyId'] = companyId
        body[0]['SameAsCompanyInd'] = 1
        response = self.compass.post(contactsUrl, json= body)
        assert response.json()[0]['CompanyAddressID'] == addressId
        contactId = response.json()[0]['ContactId']
        setup.config.cache.set('contact_id', contactId)

        #get address for new contact and validate data
        #print("New contact with linked address - ", response.json())
        global contactaddressesUrl
        contactaddressesUrl = urljoin(self.host, '/api/contacts/'+ f'{contactId}' + '/addresses')
        response = self.compass.get(contactaddressesUrl)
        assert response.json()[0]['AddressType'] == 'Office'
        assert response.json()[0]['City'] == city
        assert response.json()[0]['PostalCode'] == zip
        assert response.json()[0]['Country'] == country
        assert response.json()[0]['Phone'] == phone

    @pytest.mark.dependency(depends=["TestAddressSharing::test_contact_gets_address_from_company"])
    def test_update_company_address_reflects_to_contact(self, setup):
        addressId = setup.config.cache.get('address_id', None)
        global countryUpdate
        countryUpdate = 'Russia'
        body = [{ "AddressID": addressId, "CountryName": countryUpdate}]
        response  = self.compass.put(companyAddressesUrl, json = body)
        assert response.status_code == 200
        response = self.compass.get(contactaddressesUrl)
        assert countryUpdate in response.text

    @pytest.mark.dependency(depends=["TestAddressSharing::test_contact_gets_address_from_company"])
    def test_contact_linked_address_can_be_changed(self, setup):
        #add another address to company
        body = [json.load(open('Compass/payloads/addresses.json', 'r'))]
        newCountry = 'Congo'
        body[0]['CountryName'] = newCountry
        body[0]['defaultInd'] = False
        response = self.compass.post(companyAddressesUrl, json= body)
        addressNondefault = response.json()[0]['AddressID']
        print("Non default address id - ", addressNondefault)

        #associate new address id to contact
        contactId = setup.config.cache.get('contact_id', None)
        contactsUpdateUrl = urljoin(self.host, '/api/contacts/' + f'{contactId}')
        body = {'CompanyAddressID': addressNondefault }
        response = self.compass.put(contactsUpdateUrl, json=body)
        assert response.status_code == 200
        response = self.compass.get(contactaddressesUrl)
        addresses = response.json()
        for address in addresses:
            if address['Country'] == newCountry:
                assert address['DeleteRecord'] is False


    @pytest.mark.dependency(depends=["TestAddressSharing::test_update_company_address_reflects_to_contact"])
    def test_contact_picks_default_address(self, setup):
        #ensure new contacts get default address
        contactsUrl = urljoin(self.host, '/api/contacts')
        body = [json.load(open('Compass/payloads/contacts.json', 'r'))]
        body[0]['CompanyId'] = setup.config.cache.get('company_id', None)
        body[0]['SameAsCompanyInd'] = 1
        response = self.compass.post(contactsUrl, json= body)
        assert response.json()[0]['CompanyAddressID'] == setup.config.cache.get('address_id', None)
        
        contactId = response.json()[0]['ContactId']
        contactaddressesUrl = urljoin(self.host, '/api/contacts/'+ f'{contactId}' + '/addresses')
        response = self.compass.get(contactaddressesUrl)
        assert response.json()[0]['Country'] == countryUpdate
