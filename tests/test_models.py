import pytest

from src.pytemplate.domain.models import Operands, operands_factory


def test_operands_types():
    operands = Operands(1, 2)
    assert isinstance(operands.first_operand, int)
    assert isinstance(operands.second_operand, int)


def test_operand_values():
    operands = Operands(1, 3)
    assert operands.first_operand == 1
    assert operands.second_operand == 3


def test_return_type():
    operands = operands_factory(1, 2)
    assert isinstance(operands, Operands)


def test_floating_point_numbers():
    with pytest.raises(TypeError):
        operands_factory(1.1, 2.2)


def test_str_input():
    with pytest.raises(TypeError):
        operands_factory("one", "two")
