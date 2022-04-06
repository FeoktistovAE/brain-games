#!/usr/bin/env python
"""Must be imported by brain_calc.py."""
from random import randint


action_to_do = 'Find the greatest common divisor of given numbers.'


def expression_generator():
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    devider = 1
    deviders_list = ()
    answer = 1
    while devider <= number1:
        if number1 % devider == 0:
            deviders_list += (devider,)
        devider += 1
    for i in deviders_list:
        if number2 % i == 0:
            answer = i
    expression = str(number1) + ' ' + str(number2)
    return (answer, expression)
