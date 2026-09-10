
def users():
    u1 = ["Dimple", "Mike", "Joseph"]
    return u1


def test_users():
    u2 = users()

    assert "Mike" in u2     


def divide(a,b):
    return a/b
def test_divide():
    assert divide(10,20)


import pytest

def divide(a, b):
    return a / b


def test_divide_by_zero():
        assert divide(10, 20)
    