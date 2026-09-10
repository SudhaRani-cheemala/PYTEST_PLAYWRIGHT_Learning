from test_fixture_package import company


def test_company(company):
    assert company["name"]=="Amazon"
