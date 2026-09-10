def get_user():
    return {
       "name":"Dimple",
       "age":25,
       "City":"Hyderabad"
    }

def test_user():
    user=get_user()
    assert user["name"]=="Dimple"
    assert user["age"]==25
    assert user["City"]=="Hyderabad"






def numbers():
    assert 10==10


def test_numbers():
    assert 10!=20


def calculate_salary(basic,bonus):
    return basic+bonus

def test_salary():
    salary=calculate_salary(10000,2000)    
    assert salary==12000
    assert salary>2000

def comlist():
    acual=[1,2,3]
    expected=[1,2,3]
    assert acual==expected        



        
