#!/usr/bin/env python
"""Must be imported by brain_calc.py."""
from random import randint, choice


DESCRIPTION = 'What is the result of the expression?'


def get_random_sign(a, b):
    signs = ('+', '-', '*')
    random_sign = choice(signs)
    if random_sign == '+':
        expression = ((a + b), (str(a) + ' + ' + str(b)))
    elif random_sign == '-':
        expression = ((a - b), (str(a) + ' - ' + str(b)))
    else:
        expression = ((a * b), (str(a) + ' * ' + str(b)))
    return expression


def get_expressions():
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    return get_random_sign(number1, number2)
