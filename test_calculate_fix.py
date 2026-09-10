from calculate import add,sub,mul
import pytest
@pytest.fixture
def numbers():
    return {

      "a":10,
      "b":40
    }
def test_add(numbers):
    result=add(numbers["a"],numbers["b"])
    assert result==50