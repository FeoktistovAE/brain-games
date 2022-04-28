"""Must be imported by brain_calc.py."""
from random import randint, choice


DESCRIPTION = 'What is the result of the expression?'


def get_expression_and_result():
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    operators = ('+', '-', '*')
    random_operator = choice(operators)
    expression = f"{number1} {random_operator} {number2}"
    if random_operator == '+':
        result = number1 + number2
    elif random_operator == '-':
        result = number1 - number2
    else:
        result = number1 * number2
    return expression, result
