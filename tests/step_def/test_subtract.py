from service.subtract import subtract
from pytest_bdd import given, when, then, scenario, parsers

@scenario('test_calculator.feature', 'subtract')
def test_subtract():
    pass

@when(parsers.parse('subtracting {n1:d} and {n2:d}'), target_fixture='result')
def subtracting(n1, n2):
    result = subtract(n1, n2)
    return result
