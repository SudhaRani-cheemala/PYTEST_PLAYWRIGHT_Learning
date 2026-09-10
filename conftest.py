import pytest

@pytest.fixture
def employee():
    print("Creating employee")
    return "Dimple"