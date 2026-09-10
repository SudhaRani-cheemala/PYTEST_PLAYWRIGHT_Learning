def add(a, b):
    return a + b

def test_add():
    result = add(10, 20)
    assert result == 30
def test_add_negative_numbers():
    result=add(-5,-5)
    assert result==-10  
