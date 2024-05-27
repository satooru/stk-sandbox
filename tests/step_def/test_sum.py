from service.sum import sum
from pytest_bdd import given, when, then, scenario, parsers

@scenario('test_calculator.feature', 'sum')
def test_sum():
    pass

@when(parsers.parse('summing {n1:d} and {n2:d}'), target_fixture='result')
def summing(n1, n2):
    result = sum(n1, n2)
    return result
