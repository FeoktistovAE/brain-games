#!/usr/bin/env python
"""Must be imported by brain_calc.py."""
from random import randint, choice


GAME_DESCRIBTION = 'What is the result of the expression?'


def expressions():
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    sum = ((number1 + number2), (str(number1) + ' + ' + str(number2)))
    substraction = ((number1 - number2), (str(number1) + ' - ' + str(number2)))
    multiply = ((number1 * number2), (str(number1) + ' * ' + str(number2)))
    set_of_expressions = [sum, substraction, multiply]
    random_expression = choice(set_of_expressions)
    return random_expression
