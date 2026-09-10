
from calculate import add,sub,mul,even,positive,negative,name
def test_add():
    assert add(10,20)==30
def test_sub():
    assert sub(10,20)==-10
def test_mul():
    assert mul(10,20)==200 
def test_even():
    assert even(2,4)==0



def test_name():
    actual = name()
    print(actual)
    expected = "dimple"

    assert actual == expected