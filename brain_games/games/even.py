"""Must be imported by brain_even.py."""
from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no"'


def get_data():
    number = randint(1, 100)
    if number % 2 == 0:
        result = 'yes'
    else:
        result = 'no'
    return result, number
