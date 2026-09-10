import pytest
@pytest.mark.skip(reason='Feature is not ready')
def test_payments():
    print("Testing a payment")


import pytest

browser = "chrome"

@pytest.mark.skipif(browser == "firefox", reason="Not supported in Firefox")
def test_login():
    print("Testing login")    