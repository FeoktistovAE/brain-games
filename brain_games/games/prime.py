"""Must be imported by brain_prime.py."""
from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number < 2:
        return False
    deviders = range(2, number + 1)
    for devider in deviders:
        if number % devider == 0:
            if devider != number:
                return False
    return True


def get_expression_and_result():
    number = randint(1, 100)
    if is_prime(number):
        return number, 'yes'
    return number, 'no'
