#!/usr/bin/env python
"""Must be imported by brain_prime.py."""
from random import randint


action_to_do = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def expression_generator():
    number = randint(1, 100)
    deviders = range(1, number + 1)
    set = ()
    for i in deviders:
        if number % i == 0:
            set += (i,)
    if set == (1, number):
        answer = 'yes'
    else:
        answer = 'no'
    return answer, number
