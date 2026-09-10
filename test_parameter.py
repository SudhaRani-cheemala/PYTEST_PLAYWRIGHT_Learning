import pytest
@pytest.mark.parametrize("numbers",[1,2,3,4,5,6])
def test_numbers(numbers):
    print("Numbers :",numbers)
    assert numbers>0



@pytest.mark.parametrize("a,b,results",[
(1,2,3),
(4,5,9),
(5,5,10)
])
def test_num(a,b,results):
    print("Print results :",results)
    assert a+b==results

#Pytest parameterization is used to execute the same test case with multiple sets of test data. It helps reduce duplicate code, improves test coverage, and makes data-driven testing easier.
# Fixture = prepare something for the test
#Parameterization = run the test with different data
    
#"Parameterization in Pytest allows us to run the same test function with multiple sets of input data. We use @pytest.mark.parametrize() for this. It helps us implement data-driven testing, reduce duplicate test code, and improve test coverage."    