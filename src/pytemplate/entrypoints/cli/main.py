from pytemplate.domain.models import operands_factory
from pytemplate.service.calculator import Calculator


def main():

    available_actions = ("add", "subtract", "multiply", "divide")

    first_operand = int(input("Enter first integer number: "))
    second_operand = int(input("Enter second integer number: "))
    action = input(f"Enter one action {available_actions}: ")
    calculator = Calculator()

    if action in available_actions:
        operands = operands_factory(first_operand, second_operand)
        result = calculator.__getattribute__(action)(operands)
        print(result, end="")

    else:
        print("Invalid action name", end="")
