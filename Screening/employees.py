import pytest
import requests
import yaml

request_header = {"Accept": "application/json", "User-Agent": "XYZ"}

@pytest.fixture
def setup_url():
    '''
        Loads an environment yaml and returns a config relevant to your project based on
        the environment you are running against.
    '''
    with open("environment_config.yml") as file:
        cfg = yaml.load(file, Loader=yaml.FullLoader)
    employee_endpoint  = cfg['PRODUCTION']['service_url'] + '/api/v1/employees'
    return employee_endpoint
   
@pytest.mark.employee
def test_PrintEmployeeNameAge(setup_url):
    '''
        Query employees api and print the name and age of each on separate lines
    '''
    response = requests.get(url = setup_url, headers= request_header)
    assert response.status_code == 200
    for employee_data in response.json()['data']:
        print(employee_data['employee_name'] , "\n" ,  employee_data['employee_age'])

