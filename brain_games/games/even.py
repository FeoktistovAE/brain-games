from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no"'


def get_expression_and_result():
    number = randint(1, 100)
    if number % 2 == 0:
        return number, 'yes'
    return number, 'no'
