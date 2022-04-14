#!/usr/bin/env python
"""Must be imported by brain_gcd.py."""
from random import randint


GAME_DESCRIBTION = 'Find the greatest common divisor of given numbers.'


def gcd(number1, number2):
    devider = 1
    deviders_list = ()
    while devider <= number1:
        if number1 % devider == 0:
            deviders_list += (devider,)
        devider += 1
    for i in deviders_list:
        if number2 % i == 0:
            answer = i
    return answer


def expressions():
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    expression = str(number1) + ' ' + str(number2)
    return (gcd(number1, number2), expression)
