from locust import HttpUser, task

test_contact = {
    "CompanyId": 2651953,
    "IsActive": 1,
    "FirstName": "LOAD Alan TEST",
    "LastName": "LOAD Coffelt TEST"
}

test_lead = {"Name": "LOAD TEST 8927oisdf8"}
test_company = {"Name": "LOAD TEST 2938jfdfkr943"}
test_opp = {
    "ClientId": 6777924,
    "OpportunityName": "LOAD TEST 827348923"
}

test_call = {
    "subject": "LOAD TEST 82394892384"
}

test_project = {
    "ProjectName": "LOAD TEST 829384984"
}

class theTest(HttpUser):
    min_wait = 500
    max_wait = 1500

    host = "http://newtours.demoaut.com" # can be given in UI or cmdline as well

    creds =  {
        'accept': 'application/json',
        'x-compass-firm-id': '822',
        'Authorization': 'Basic cmxld2lzOlFDMkVWS0hQNnpzOGJ1RTJecEJyTlh0eg==',
        'x-compass-api-key': 'dbf97abb-6905-42c7-b645-f8941a225fe7'
    }

# use task sequence for things in serial order

    @task
    def launch_url(self):
        self.client.get("/")

    @task(1)                      # Enables tasks inside taskset class with weightage
    def paging_contacts(self):
        fr = 0
        while True:
            print(f">> paging contacts at {fr}")
            r = self.client.get(f"/api/contacts?from={fr}&size=200&full=true", headers=self.creds)
            if r.text == '[]':
                break
            else:
                fr = fr + 200

    # @task
    # def write_contact(self):
    #     r = self.client.post(f"/api/contacts", headers=self.creds, json=[test_contact])
    #     if r.status_code != 200:
    #         print(r.text)

    # @task
    # def write_leads(self):
    #     r = self.client.post(f"/api/leads", headers=self.creds, json=[test_lead])
    #     if r.status_code != 200:
    #         print(r.text)

    # @task
    # def write_companies(self):
    #     r = self.client.post("/api/companies", headers=self.creds, json=[test_company])
    #     if r.status_code != 200:
    #         print(r.text)

    @task
    def paging_companies(self):
        fr = 0
        while True:
            print(f">> paging companies at {fr}")
            r = self.client.get(f"/api/companies?from={fr}&size=200", headers=self.creds)
            if r.text == '[]':
                break
            else:
                fr = fr + 200

    @task
    def paging_opportunities(self):
        fr = 0
        while True:
            print(f">> paging opportunities at {fr}")
            r = self.client.get(f"/api/opportunities?from={fr}&size=200", headers=self.creds)
            if r.text == '[]':
                break
            else:
                fr = fr + 200

    @task
    def paging_leads(self):
        fr = 0
        while True:
            print(f">> paging leads at {fr}")
            r = self.client.get(f"/api/leads?from={fr}&size=200", headers=self.creds)
            if r.text == '[]':
                break
            else:
                fr = fr + 200

    @task
    def paging_projects(self):
        fr = 0
        while True:
            print(f">> paging projects at {fr}")
            r = self.client.get(f"/api/projects?from={fr}&size=200", headers=self.creds)
            if r.text == '[]':
                break
            else:
                fr = fr + 200

    @task
    def paging_calllogs(self):
        fr = 0
        while True:
            print(f">> paging call logs at {fr}")
            r = self.client.get(f"/api/calllogs?from={fr}&size=200", headers=self.creds)
            if r.text == '[]':
                break
            else:
                fr = fr + 200

    @task
    def paging_personnel(self):
        fr = 0
        while True:
            print(f">> paging personnel at {fr}")
            r = self.client.get(f"/api/personnel?from={fr}&size=200", headers=self.creds)
            if r.text == '[]':
                break
            else:
                fr = fr + 200
