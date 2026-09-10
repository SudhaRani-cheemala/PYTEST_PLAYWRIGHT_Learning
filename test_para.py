import pytest
@pytest.mark.parametrize("username",[
    "admin",
    "user1",
    "user2"])
def test_login(username):
    print("login with: ",username)


@pytest.mark.parametrize("username,password",[

("admin","admin1"),
("dev","dev1"),
("tester","test1")

])

def user_login(username,password):
    print("Employees login details")
    assert username is not None
    assert password is not None


