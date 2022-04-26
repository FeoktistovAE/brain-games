"""Must be imported by brain_calc.py."""
from random import randint, choice


DESCRIPTION = 'What is the result of the expression?'


def get_data():
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    signs = ('+', '-', '*')
    random_sign = choice(signs)
    if random_sign == '+':
        expression = (number1 + number2, (str(number1) + ' + ' + str(number2)))
    elif random_sign == '-':
        expression = (number1 - number2, (str(number1) + ' - ' + str(number2)))
    else:
        expression = (number1 * number2, (str(number1) + ' * ' + str(number2)))
    return expression
