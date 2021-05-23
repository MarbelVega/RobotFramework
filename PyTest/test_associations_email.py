import base64
import json
import re
from urllib.parse import urljoin

import pytest
import requests
from IntegrationConfigManager import IntegrationConfigManager

pytestmark = [pytest.mark.compass, pytest.mark.associations, pytest.mark.emailattachments]
class TestEmailAttachment:

    @pytest.fixture
    def setup(self, request):
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

        # create an email
        emailUrl = urljoin(self.host, '/api/emails')
        body = [json.load(open('Compass/payloads/emails.json', 'r'))]
        response = self.compass.post(emailUrl, json=body)
        assert response.status_code == 200
        emailId = response.json()[0]['Id']

        # create attachment obj for the email
        attachmentObjectUrl = urljoin(self.host, f'/api/emails/{emailId}/attachments')
        body = [{"FileName": "testFile.txt"}]
        response = self.compass.post(attachmentObjectUrl, json=body)
        assert response.status_code == 200
        assert "testFile.txt" in response.text

        # Once the attachment object is created, use file endpoint to read/write data
        self.attachmentFileEndpoint = response.json()[0]['AttachmentEndpoint']
        print('Attachment endpoint - ', self.attachmentFileEndpoint)

    def test_create_attachment_formdata(self, setup):
        # create file data using Multipart form data
        attachmentUrl = urljoin(self.host, self.attachmentFileEndpoint)
        myFile = {"file": open('Compass/payloads/testFile.txt', "rb")}
        response = self.compass.post(attachmentUrl, files=myFile,
                                     headers={'Content-Type': 'multipart/form-data',
                                              'boundary': '----WebKitFormBoundary7MA4YWxkTrZu0gW'})
        assert response.status_code == 200
        assert 'CommonProgramW6432' in self.compass.get(attachmentUrl).text

    def test_create_attachment_url(self, setup):
        # create file data using url parameter in the query string
        attachmentUrl = urljoin(self.host, self.attachmentFileEndpoint)
        filePath = 'http://www.sci.utah.edu/~macleod/docs/txt2html/sample.txt'
        # Other samples https://file-examples-com.github.io/uploads/2017/02/file-sample_100kB.doc
        response = self.compass.post(attachmentUrl, params={'url': filePath})
        assert response.status_code == 200
        assert 'TextToHTML' in self.compass.get(attachmentUrl).text

    def test_create_attachment_base64encoded(self, setup):
        # here we base64 encode our text file and send the data as string in a JSON object
        attachmentUrl = urljoin(self.host, self.attachmentFileEndpoint)
        myFile = open('Compass/payloads/testFile.txt', "rb").read()
        encodedData = {'Data': base64.b64encode(myFile).decode('UTF-8')}
        response = self.compass.post(attachmentUrl, json=encodedData)
        assert response.status_code == 200
        # verify binary data contents
        assert 'CommonProgramW6432' in self.compass.get(attachmentUrl).text
        # verify JSON object in base64 encoded
        response = self.compass.get(attachmentUrl, headers={'Accept': 'application/json'})
        assert response.status_code == 200
        assert response.json() == encodedData

    def test_update_attachment(self, setup):
        # verify attachments using PUT call
        attachmentUrl = urljoin(self.host, self.attachmentFileEndpoint)
        fileUpdate = 'https://www.cosential.com/wp-content/uploads/2020/09/Cosential-Product-Overview_Outlook-2.pdf'
        response = self.compass.put(attachmentUrl, params={'url': fileUpdate})
        assert response.status_code == 200

    def test_delete_attachment(self, setup):
        # verify deleting attachment object
        attachmentObject = re.sub("attachmentfile", "attachments", self.attachmentFileEndpoint)
        response = self.compass.delete(urljoin(self.host, attachmentObject))
        assert response.status_code == 200
