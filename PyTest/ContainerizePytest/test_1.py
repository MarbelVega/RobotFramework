import pytest

@pytest.fixture()
def setup(request):
    print("BEFORE METHOD")
    request.config.cache.set("shared", "fixture")
    return request
    # yield
    # print("AFTER METHOD")

@pytest.fixture()
def data():
    return [0,2,4]

@pytest.fixture(params=[
    {'user':'user1', 'password':'pwd1'},
    {'user':'user2', 'password':'pwd2'},
])
def data_provider(request):
    return request.param



def test_1(setup):
    print("TEST METHOD 1")
    print("SUCCESS IF FIXTURE", setup.config.cache.get("shared", None))
    setup.config.cache.set("shared", "blah")


@pytest.mark.usefixtures('data')
class TestPy:
    @pytest.mark.usefixtures('setup')              # usefixtures on method is same as passing the name as param test_2(setup)
    def test_2(self, data):
        print("CLASS TEST METHOD")
        print(data[1])

    @pytest.mark.usefixtures('data_provider')
    def test_3(self, data_provider):               # test3 executes twice
        print(data_provider['user'])
        print(data_provider['password'])
