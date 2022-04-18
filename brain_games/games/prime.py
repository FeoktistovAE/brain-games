#!/usr/bin/env python
"""Must be imported by brain_prime.py."""
from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    deviders = range(1, number + 1)
    without_remainder = ()
    for i in deviders:
        if number % i == 0:
            without_remainder += (i,)
    if without_remainder == (1, number):
        answer = True
    else:
        answer = False
    return answer


def get_expressions():
    number = randint(1, 100)
    if is_prime(number) is True:
        answer = 'yes'
    else:
        answer = 'no'
    return answer, number
