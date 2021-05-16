from locust import HttpLocust, TaskSet, between
import base64

# setup, teardown

'''
HttpLocust inherits clients which creates http session.
The same client is returned by self.client in Task set
'''

def login(l):
    l.client.post('/index.', {'username': 'akulkarni', 'password': 'QC2EVKHP6zs8buE2^pBrNXtz', 'firmid': '822'})

def logout(l):
    l.client.post('/logout.', {'logout': 'true'})

# quick search

def quick_search(l):
    payload = {"quick-search-type": "all", "quick-search-query": "test"}
    with l.client.post('/search', data=payload, catch_response=True) as r:          # only specify path that comes after host here
        print(r.text)
        verify_text_is_on_page("not what you", r, " search did not work as expected.")

# view pages

def project_view(l):
    with l.client.get('/projects/project_view.?projectID=1213683', catch_response=True) as r:
        verify_text_is_on_page("published project name", r, "Project View page did not work as expected.")

def opportunity_view(l):
    with l.client.get('/contact/lead_view.?leadid=1930026', catch_response=True) as r:
        verify_text_is_on_page("stage history", r, "Opportunity View page did not work as expected.")

def company_view(l):
    with l.client.get('/contact/company_view.?CompanyID=2171827', catch_response=True) as r:
        print(r.text)
        verify_text_is_on_page("Affiliate Contacts", r, "Company View page did not work as expected.")

def personnel_view(l):
    with l.client.get('/templates/glbPersonnel_set_Session.?PersonnelID=1221705', catch_response=True) as r:
        verify_text_is_on_page("Office Contact Info", r, "Personnel view page did not work as expected.")

def contact_view(l):
    with l.client.get('/contact/contact_view.?individualid=3354631', catch_response=True) as r:
        verify_text_is_on_page("Affiliate Companies", r, "Contact View did not load.")

def lead_view(l):
    with l.client.get('/contact/oppLead_view.?oppleadid=1395253', catch_response=True) as r:
        verify_text_is_on_page("Associated Events", r, "Lead View did not load.")

# read/write images

def view_project_image(l):
    with l.client.get('/projects/projimages/download_full_image.?FileID=KbRP9D9NQBp0jhNDkGqzvZpyNBgg~~&View=true', catch_response=True) as r:
        if r.status_code == 200:
            r.success()
        else:
            r.failure("Did not view the project image.")

# def post_project_image(l):
#     with l.client.post('/com/model/project/projectImages.cfc?method=processImage&requestTimeout=10000&token=7B4267ED5C4C464397D208CC74CCDB54',
#         files={"UploadFile_0": ("duck.jpg", open("duck.jpg", "rb"), "image/jpeg")}, catch_response=True) as r:
#         if r.status_code == 200:
#             r.success()
#         else:
#             r.failure("Did not upload the project image.")
# grid datas

def project_grid_data(l):
    # look into random sorts, random startsWith's, maybe.
    payload={
        "sort": "ownerName",
        "dir": "ASC",
        "start": 0,
        "limit": 50,
        "startsWith": "",
        "method": "doAction"
    }
    with l.client.post('/com/model/project/projectGridProxy.cfc', data=payload, catch_response=True) as r:
        verify_grid_data_has_landed(r, "Projects grid data did not return as expected.")

def contact_grid_data(l):
    payload={
        "sort": "firstname",
        "dir": "ASC",
        "start": 0,
        "limit": 50,
        "startsWith": "",
        "UserId": "[]",
        "IncludeDeleted": "false",
        "IncludeInactive": "false",
        "KeyContact": "false"
    }
    with l.client.post('/com/model/contact/contact.cfc?method=getGridData', data=payload, catch_response=True) as r:
        verify_grid_data_has_landed(r, "Contact grid data did not return as expected.")

def index(l):
    r = l.client.get('/dashboard/widgets/fulltab/client_excellence/details-print.cfm?id=4919797&iFrameMode=false')
    print("DB16-TEXAS A&M COOPERATIVE EDUCATION" not in r.text)

def lead_grid_data(l):
    payload={
        "start": 0,
        "limit": 500,
        "sort": "createdate",
        "dir": "DESC",
        "bidDate": "",
        "createDtEnd": "",
        "score": "",
        "stage": "",
        "territory": "",
        "oppDate": "",
        "costMin": 0,
        "division": "",
        "client": "",
        "createDtStart": "",
        "unassigned": "",
        "status": "1,3",
        "personnel": "",
        "practiceArea": "",
        "officeDivision": "",
        "office": "",
        "source": "",
        "leadStatus": 1,
        "costOp": "",
        "tip": '<div style="padding-top: 5px;"><div>Stage: All</div><div>Source: All</div><div>Score: All</div></div>',
        "serviceType": "",
        "costMax": "-1",
        "studio": "",
        "query": "",
        "pageSize": 500,
        "method": "search",
        "xaction": "read"
    }

    with l.client.post('/com/model/lead/lead.cfc', data=payload, catch_response=True) as r:
        verify_grid_data_has_landed(r, "Leads grid data did not return as expected.")

def opportunity_grid_data(l):
    number_of_records = 500 # 25, 50, 100, or 500
    payload={
        "start": 0,
        "limit": number_of_records,
        "action": "getOpportunityGridData",
        "json": 1,
        "sort": "ACTIVEIND",
        "dir": "ASC",
        "view": 0,
        "ActiveInd": 0,
        "SalesCycle": "NaN",
        "officeId": 0,
        "divisionId": 0,
        "studioId": 0,
        "practiceAreaId": 0,
        "territoryId": 0,
        "stageId": 0,
        "priCatId": 0,
        "secCatId": 0,
        "masterSub": 0,
        "staffRoleId": 0,
        "dateCreated": 0,
        "dateModified": 0,
        "dateCreatedModified": 0,
        "filteredSearch": 0,
        "search": ""
    }

    with l.client.post('/contact/opportunity/oppActions.', data=payload, catch_response=True) as r:
        verify_grid_data_has_landed(r, "Opportunity grid data did not return as expected.")

def call_log_grid_data(l):
    payload = {
        "method": "getGridData",
        "xaction": "read"
    }
    with l.client.post('/com/model/activities/callLog.cfc', data=payload, catch_response=True) as r:
        verify_grid_data_has_landed(r, "Call Log grid data did not return as expected.")

def task_grid_data(l):
    payload = {
        "method": "search",
        "taskOwnerFilter": 2
    }
    with l.client.post('/com/model/task/task.cfc', data=payload, catch_response=True) as r:
        verify_grid_data_has_landed(r, "Task grid data did not return as expected.")

# reporting engine

def report_projects_long_running(l):
    with l.client.get('/reports20/ReportsResults.?ReportID=KbRP9DuUxpeAQ6Cviu8L9dOwYYNA~~&ReportTypeID=1', catch_response=True) as r:
        verify_text_is_on_page("Report Run Time", r, "Long Running Project Report 1 did not load.")


# verifies for these simple tests.

def verify_grid_data_has_landed(page, error_message):
    if page.status_code == 200 and "There was an error" not in page.text:
        page.success()
    else:
        page.failure(error_message)

def verify_text_is_on_page(text, page, error_message):
    if text.lower() in page.text.lower():
        page.success()
    else:
        page.failure(error_message)

# define tasks here as dict with weightage same as @task(1)

class UserBehavior(TaskSet):
    tasks = {
        project_view: 1,
        quick_search: 1,
        lead_view: 1,
        contact_view: 1,
        company_view: 1,
        personnel_view: 1,
        opportunity_view: 1,
        view_project_image: 1,
        project_grid_data: 1,
        contact_grid_data: 1,
        opportunity_grid_data: 1,
        lead_grid_data: 1,
        call_log_grid_data: 1,
        task_grid_data: 1,
        report_projects_long_running: 1,
        # post_project_image: 1

    }

# execute only once
    def on_start(self):
        login(self)
        # use list of tuples for diff users but ensure no. of users doesn't exceed the swarm no given

    def on_stop(self):
        logout(self)


# define user
class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    wait_time = between(5.0, 8.0)   # wait time between tasks

