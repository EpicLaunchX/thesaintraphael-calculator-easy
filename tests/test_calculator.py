from src.pytemplate.domain.models import operands_factory
from src.pytemplate.service.calculator import Calculator


def test_add():
    assert Calculator().add(operands_factory(10, 20)) == 30


def test_subtract():
    assert Calculator().subtract(operands_factory(10, 20)) == -10


def test_multiply():
    assert Calculator().multiply(operands_factory(10, 20)) == 200


def test_divide():
    assert Calculator().divide(operands_factory(20, 10)) == 2


def test_divide_with_small_divisor():
    assert Calculator().divide(operands_factory(10, 20)) == 0


def test_divide_with_not_exact_division():

    result = Calculator().divide(operands_factory(10, 3))

    assert isinstance(result, int)
