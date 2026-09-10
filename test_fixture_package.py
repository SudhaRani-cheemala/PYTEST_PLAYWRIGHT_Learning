import pytest
@pytest.fixture(scope='package')

def company():
    print("Hello this is amazon")
    com={

       "name":"Amazon",
       "country":"USA",
       "Year":1970

    }

    yield com

print("Deleting company")

