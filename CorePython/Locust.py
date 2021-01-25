
from locust import HttpUser,task

class inherit(HttpUser):

    @task
    def companydetails(self):

            test_name = "CFO-BFFE Company Details"

            r = self.client.req