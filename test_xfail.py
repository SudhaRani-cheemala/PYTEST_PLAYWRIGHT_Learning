import pytest


@pytest.mark.skip(reason="Feature not ready")
def test_payment():
    assert 1 == 1


@pytest.mark.xfail(reason="Known bug")
def test_login():
    assert 1 == 2


def test_homepage():
    assert 1 == 1
