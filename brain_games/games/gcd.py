"""Must be imported by brain_gcd.py."""
from random import randint


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def gcd(number1, number2):
    devider = 1
    deviders_list = ()
    while devider <= number1:
        if number1 % devider == 0:
            deviders_list += (devider,)
        devider += 1
    for i in deviders_list:
        if number2 % i == 0:
            result = i
    return result


def get_data():
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    expression = f"{number1} {number2}"
    return (gcd(number1, number2), expression)
