import pytest


@pytest.fixture
def user():
    return {"Name": "Dimple", "Age": 25}


def test_user_name(user):
    assert user["Name"] == "Dimple"
    assert user["Age"] == 25