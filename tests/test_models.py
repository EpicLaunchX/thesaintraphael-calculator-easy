from src.pytemplate.domain.models import Operands


def test_operands_types():
    operands = Operands(1, 2)
    assert isinstance(operands.first_operand, int)
    assert isinstance(operands.second_operand, int)


def test_operand_values():
    operands = Operands(1, 3)
    assert operands.first_operand == 1
    assert operands.second_operand == 3
