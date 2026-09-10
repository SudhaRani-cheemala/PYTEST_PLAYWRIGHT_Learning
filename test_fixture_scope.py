#function  → runs for every test


import pytest
@pytest.fixture
def employee():
    print("Employee details")
    emp={

       "Name":"Dimple",
       "Age":25
    }
    yield emp
    print("Delete Employee data")


def test_one(employee):
    assert employee["Name"]=="Dimple"

def test_two(employee):
    assert employee["Age"]==25

    








# class     → runs once per test class
# module    → runs once per Python test file
# session   → runs once for the entire pytest run

