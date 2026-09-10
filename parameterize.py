import pytest
@pytest.mark.parametrize("username",[
    "admin",
    "user1",
    "user2"])
def test_login(username):
    print("login with: ",username)