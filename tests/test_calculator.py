from src.pytemplate.domain.models import operands_factory
from src.pytemplate.service.calculator import Calculator


def test_addition():
    assert Calculator().add(operands_factory(10, 20)) == 30


def test_subtraction():
    assert Calculator().subtract(operands_factory(10, 20)) == -10


def test_multiplication():
    assert Calculator().multiply(operands_factory(10, 20)) == 200


def test_division():
    assert Calculator().divide(operands_factory(20, 10)) == 2


def test_division_should_return_zero_when_divisor_is_greater_than_dividend():
    assert Calculator().divide(operands_factory(10, 20)) == 0


def test_division_should_return_correct_floor_integer_when_division_is_not_exact():

    result = Calculator().divide(operands_factory(10, 3))

    assert isinstance(result, int)
