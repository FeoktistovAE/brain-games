"""Must be imported by brain_prime.py."""
from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    deviders = range(1, number + 1)
    for devider in deviders:
        if number % devider == 0:
            if devider != 1 and devider != number:
                return False
    return True


def get_data():
    number = randint(1, 100)
    if is_prime(number) is True:
        result = 'yes'
    else:
        result = 'no'
    return result, number
