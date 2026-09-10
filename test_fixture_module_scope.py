import pytest
@pytest.fixture(scope='module')
def employee():
    print("Employee details")
    emp={
        "Name":"Sudha",
        "Age":20,
        "Gender":"F"

    }

    yield emp
    print("Delete Employee data")


def test_name(employee):
    assert employee["Name"]=="Sudha"


class TestEmployeedetails:
    def test_two(self,employee):
        assert employee["Age"]==20

