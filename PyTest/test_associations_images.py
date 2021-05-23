import base64
import json
from urllib.parse import urljoin, urlparse

import pytest
import requests
from IntegrationConfigManager import IntegrationConfigManager

tests = [

    ## Images associated with contacts #############################################################################
    pytest.param('contacts', 'ContactId', 'cardfront',
                 marks=[pytest.mark.compass, pytest.mark.associations, pytest.mark.contactimages]),
    pytest.param('contacts', 'ContactId', 'cardback',
                 marks=[pytest.mark.compass, pytest.mark.associations, pytest.mark.contactimages]),
    pytest.param('contacts', 'ContactId', 'profilepicture',
                 marks=[pytest.mark.compass, pytest.mark.associations, pytest.mark.contactimages]),

    ## Images associated with companies #############################################################################
    pytest.param('companies', 'CompanyId', '',
                 marks=[pytest.mark.compass, pytest.mark.associations, pytest.mark.companyimages]),

]


@pytest.mark.parametrize('parent, parent_pk, child', tests)
class TestImages:

    @pytest.fixture
    def setup(self, parent, parent_pk):
        # Load the config
        ccm = IntegrationConfigManager()
        config = ccm.load_config()

        # Load the environment data
        api_key = config["api_keys"][0]
        firmid = str(config["default_firmid"])
        self.host = config["service_url"]
        print(self.host)

        default_user = ccm.load_user(
            firm_id=firmid,
            user_type=['Administrator', 'OFA', 'RW User']
        )
        user = (default_user["username"], default_user["password"])

        # Set up compass to work with everything
        self.compass = requests.Session()
        self.compass.verify = False
        self.compass.auth = user
        self.compass.headers.update({
            "x-compass-firm-id": firmid,
            "x-compass-api-key": api_key,
            "Content-Type": "application/json"
        })

        # retrieve a parent record to operate on
        parentUrl = urljoin(self.host, f'api/{parent}')
        response = self.compass.get(parentUrl)
        assert response.status_code == 200
        if len(response.json()) == 0:
            pytest.skip(f'Skipping test - No {parent} records')

        self.recordId = response.json()[0][parent_pk]
        print(f'{parent} retrieved - {self.recordId}')

        # contacts endpoint is api/contacts/ while images is api/images/contact/... hence change parent here
        if parent == 'contacts':
            parent = 'contact'
        return parent

    def test_update_image_url(self, setup, child):
        # upload image using url parameter in the query string
        imageUrl = urljoin(self.host, f'/api/images/{setup}/{self.recordId}/{child}')
        filePath = 'https://unanet.com/icons/icon-384x384.png'
        print("Image URL - ", imageUrl)
        response = self.compass.put(imageUrl, params={'url': filePath})
        assert response.status_code == 200

    def test_update_image_base64encoded(self, setup, child):
        # here we base64 encode our image and send the data as string in a JSON object
        imageUrl = urljoin(self.host, f'/api/images/{setup}/{self.recordId}/{child}')
        myFile = open('Compass/payloads/GovCon.jpg', "rb").read()
        encodedData = {'ContentType': 'image/jpeg', 'Data': base64.b64encode(myFile).decode('UTF-8')}
        response = self.compass.post(imageUrl, json=encodedData)
        assert response.status_code == 200

    def test_update_image_formdata(self, setup, child):
        # create file data using Multipart form data
        imageUrl = urljoin(self.host, f'/api/images/{setup}/{self.recordId}/{child}')
        print(imageUrl)
        myFile = {'File': ('GovCon', open('Compass/payloads/GovCon.jpg', 'rb'), 'image/jpeg')}
        # This endpoint does not work well with header ={'Content-Type': 'multipart/form-data','boundary': '----WebKitFormBoundary7MA4YWxkTrZu0gW'})
        # Alternate way is sending file as binary data. - myFile = open('payloads/GovCon.jpg', 'rb').read() and use above headers.
        self.compass.headers['Content-Type'] = None
        response = self.compass.post(imageUrl, files=myFile)
        assert response.status_code == 200

tests_p = [

    ## Images associated with projects #############################################################################
    pytest.param('projects', 'ProjectId',
                 marks=[pytest.mark.compass, pytest.mark.associations, pytest.mark.projectimages]),

    # Needs work due to BE-333
    # ## Images associated with personnel #############################################################################
    pytest.param('personnel', 'PersonnelId',
                 marks=[pytest.mark.compass, pytest.mark.associations, pytest.mark.personnelimages, pytest.mark.failing]),

]


@pytest.mark.parametrize('parent, parent_pk', tests_p)
class TestImagesProjectsnPersonnel:

    @pytest.fixture
    def setup(self, parent, parent_pk):
        # Load the config
        ccm = IntegrationConfigManager()
        config = ccm.load_config()

        # Load the environment data
        api_key = config["api_keys"][0]
        firmid = str(config["default_firmid"])
        self.host = config["service_url"]
        print(self.host)

        default_user = ccm.load_user(
            firm_id=firmid,
            user_type=['OFA']  # change to ['Administrator', 'OFA', 'RW User'] after env issues resolve
        )
        user = (default_user["username"], default_user["password"])

        # Set up compass to work with everything
        self.compass = requests.Session()
        self.compass.verify = False
        self.compass.auth = user
        self.compass.headers.update({
            "x-compass-firm-id": firmid,
            "x-compass-api-key": api_key,
            "Content-Type": "application/json"
        })

        # retrieve a parent record to operate on
        parentUrl = urljoin(self.host, f'/api/{parent}')
        print("PARENT URL - ", parentUrl)
        response = self.compass.get(parentUrl)
        assert response.status_code == 200
        if len(response.json()) == 0:
            pytest.skip(f'Skipping test - No {parent} records')

        self.recordId = response.json()[0][parent_pk]
        print(f'{parent} retrieved - {self.recordId}')

        self.pImageUrl = urljoin(self.host, f'/api/{parent}/{self.recordId}/images')

        body = json.load(open('Compass/payloads/images-metadata.json', 'r'))
        response = self.compass.post(self.pImageUrl, json=body)
        pImageOperateUrl = response.json()[0]['OriginalImageEndpoint']
        parsed = urlparse(pImageOperateUrl)
        self.imageUrl = f'{parsed.scheme}://{parsed.hostname}{parsed.path}'  # remove port numbers

    def test_create_image_url_and_read(self, setup, parent):
        # upload image using url parameter in the query string
        print("Image URL - ", self.imageUrl)
        filePath = 'https://unanet.com/icons/icon-384x384.png'
        response = self.compass.put(self.imageUrl, params={'url': filePath})
        assert response.status_code in (200, 204)
        # get original image here itself since we have url ready. Another test for get will yield us null due to fixture
        response = self.compass.get(self.imageUrl, headers={'Accept': 'application/json'})
        assert response.status_code in (200, 204)
        assert 'Data' in response.json()
        assert 'ContentType' in response.json()

    def test_create_image_formdata_and_read_web(self, setup):
        # create file data using Multipart form data

        print("Image URL - ", self.imageUrl)
        myFile = {'File': ('GovCon', open('Compass/payloads/GovCon.jpg', 'rb'), 'image/jpeg')}
        # This endpoint does not work well with header ={'Content-Type': 'multipart/form-data','boundary': '----WebKitFormBoundary7MA4YWxkTrZu0gW'})
        # Alternate way is sending file as binary data. - myFile = open('payloads/GovCon.jpg', 'rb').read() and use above headers.
        self.compass.headers['Content-Type'] = None
        response = self.compass.put(self.imageUrl, files=myFile)
        assert response.status_code == 200
        # get images sized for web
        response = self.compass.get(self.imageUrl + '/web', headers={'Accept': 'image/png'}, params={'maxWidth': 50})
        assert response.status_code == 200

    def test_create_image_base64encoded_and_read_thumbnail(self, setup):
        # here we base64 encode our image and send the data as string in a JSON object
        print("Image URL - ", self.imageUrl)
        myFile = open('Compass/payloads/GovCon.jpg', "rb").read()
        encodedData = {'ContentType': 'image/jpeg', 'Data': base64.b64encode(myFile).decode('UTF-8')}
        response = self.compass.put(self.imageUrl, json=encodedData)
        assert response.status_code == 200
        # get thumbnails
        response = self.compass.get(self.imageUrl + '/thumb', headers={'Accept': 'image/png'},
                                    params={'maxHeight': 65, 'jpegQuality': 70})
        assert response.status_code == 200

    def test_update_image_metadata(self, setup):
        # only update image metadata. update image binary data happens with PUT call which we already use for create
        body = json.load(open('Compass/payloads/images-metadata.json', 'r'))[0]
        body['Caption'] = 'Small Building'
        body['IsWebsiteThumbnail'] = True
        imageId = self.imageUrl.split('/')[-1]
        print("Image URL - ", self.imageUrl)
        response = self.compass.put(self.pImageUrl + '/' + imageId, json=body)
        assert response.status_code == 200
        assert response.json()['Caption'] == 'Small Building'
        assert response.json()['IsWebsiteThumbnail'] is not False
        assert response.json()['ImageId'] == int(imageId)

    def test_delete_image_metadata(self, setup):
        # request to the image metadata endpoint will delete the metadata AND the image itself
        imageId = self.imageUrl.split('/')[-1]
        print("Image URL - ", self.imageUrl)
        response = self.compass.delete(self.pImageUrl + '/' + imageId)
        assert response.status_code == 200
        assert response.text == f'"Project Image [{imageId}] has been deleted"'
        assert self.compass.get(self.pImageUrl + '/' + imageId).text == 'null'

    def test_search_image_simple(self, setup, parent):
        # list parameter doesn't do anything hence skipping
        imageId = self.imageUrl.split('/')[-1]
        searchUrl = urljoin(self.host, f'/api/{parent}/images/search')
        print("Search URL - ", searchUrl)
        response = self.compass.get(searchUrl, params={'q': 'BITMASONS'})
        assert response.status_code == 200
        assert len(response.json()) > 0
        assert str(imageId) in response.text

    # NEEDS WORK REFER BE-330
    @pytest.mark.failing
    def test_search_project_image_exact(self, setup, parent):
        # list parameter doesn't do anything hence skipping
        imageId = self.imageUrl.split('/')[-1]
        searchUrl = urljoin(self.host, f'/api/{parent}/images/search')
        print("Search URL - ", searchUrl)
        response = self.compass.get(searchUrl,  params={'q': 'IsWebsiteImage:true'})
        assert response.status_code == 200
        assert len(response.json()) > 0
        assert str(imageId) in response.text
        assert 'blue,sky' in response.text
        response = self.compass.get(searchUrl,  params={'q': 'IsWebsiteImage:false'})
        print(len(response.json()))
        assert str(imageId) not in response.text

    @pytest.mark.failing
    def test_search_deleted_project_image(self, setup, parent):
        # list parameter doesn't do anything hence skipping

        imageId = self.imageUrl.split('/')[-1]
        print(imageId)
        # response = self.compass.delete(self.pImageUrl + '/' + imageId)
        #assert response.status_code == 200

        searchUrl = urljoin(self.host, f'/api/{parent}/images/search')
        print("Search URL - ", searchUrl)
        response = self.compass.get(searchUrl,  params={'q': 'Building', 'includeDeleted': True})
        assert response.status_code == 200
        assert len(response.json()) > 0
        assert str(imageId) in response.text

    @pytest.mark.failing
    def test_search_project_image_phrase(self, setup, parent):
        # list parameter doesn't do anything hence skipping
        imageId = self.imageUrl.split('/')[-1]
        searchUrl = urljoin(self.host, f'/api/{parent}/images/search')
        print("Search URL - ", searchUrl)
        response = self.compass.get(searchUrl,  params={'q': 'Caption:"Big-Building-Site"'})
        assert response.status_code == 200
        assert len(response.json()) > 0
        assert str(imageId) in response.text

    @pytest.mark.failing
    def test_search_project_image_wildcards(self, setup, parent):
        # list parameter doesn't do anything hence skipping
        imageId = self.imageUrl.split('/')[-1]
        searchUrl = urljoin(self.host, f'/api/{parent}/images/search')
        print("Search URL - ", searchUrl)
        response = self.compass.get(searchUrl,  params={'q': 'Caption:"Big-Building-Site"'})
        assert response.status_code == 200
        assert len(response.json()) > 0
        assert str(imageId) in response.text
