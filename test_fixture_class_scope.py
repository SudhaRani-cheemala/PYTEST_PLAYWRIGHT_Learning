import pytest
@pytest.fixture(scope='class')

def employee():
    print("Employee Details")
    emp={

        "Name":"Sudha",
        "Age":26,
        "Gender":"F"
    }

    yield emp

    print("Deleting employee details")


class TestEmployeeDetails:
    def test_name(self,employee):
        assert employee["Name"]=="Sudha"
    def test_age(self,employee):
        assert employee["Age"]==26