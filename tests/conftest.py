from pytest import fixture
from pytest_bdd import then, parsers

@then(parsers.parse('result should be {n1:d}'), target_fixture='result')
def result(result, n1):
    assert result == n1