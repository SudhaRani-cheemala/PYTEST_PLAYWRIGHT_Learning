import pytest
@pytest.fixture
def employees():
    print("Employeess details")
    employees={

        "name":"Dimple",
        "Salary":40

    }

    return employees

    print("Deleting Employess")

def test_emp(employees):
    assert employees["name"]=="Dimple"
    assert employees["Salary"]==40
    



