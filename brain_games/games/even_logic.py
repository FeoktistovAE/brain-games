#!/usr/bin/env python
"""Must be imported by brain_even.py."""
from random import randint


PRINT_ACTION = 'Answer "yes" if the number is even, otherwise answer "no"'


def expressions():
    number = randint(1, 100)
    if number % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    random_expression = (answer, number)
    return random_expression
