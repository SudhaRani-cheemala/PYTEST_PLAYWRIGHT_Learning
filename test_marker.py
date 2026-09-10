import pytest

@pytest.mark.smoke
def test_login():
    pass


@pytest.mark.smoke
def test_logout():
    pass


@pytest.mark.regression
def test_payment():
    pass


#A marker is used to add a label to a test.
#syntax: @pytest.mark.marker_name
#The main reason is to group and selectively execute tests.
#pytest -m smoke
#smoke,regression,sanity,login,payment,api,ui
#pytest dont know what these smoke,regression tests thats why we should create a file calles pytest.ini and insert below code into it
#[pytest]
# markers =
#     smoke: marks tests as smoke tests
#     regression: marks tests as regression tests

