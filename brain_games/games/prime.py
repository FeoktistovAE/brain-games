"""Must be imported by brain_prime.py."""
from random import randint
import math


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number < 2:
        return False
    deviders = range(2, int(math.sqrt(number)) + 1)
    for devider in deviders:
        if number % devider == 0:
            return False
    return True


def get_expression_and_result():
    number = randint(1, 100)
    if is_prime(number):
        return number, 'yes'
    return number, 'no'
