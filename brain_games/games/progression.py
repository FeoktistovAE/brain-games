#!/usr/bin/env python
"""Must be imported by brain_progression.py."""
from random import randint, choice


DESCRIPTION = 'What number is missing in the progression?'


def get_expressions():
    first_value = randint(1, 70)
    last_value = 150
    step = randint(2, 9)
    spread = randint(6, 11)
    random_choice = choice(range(spread))
    consequence = range(first_value, last_value, step)
    progression = ''
    for index in range(spread):
        if index == random_choice:
            answer = consequence[index]
            current_value = '..'
        else:
            current_value = str(consequence[index])
        progression += current_value + ' '
    return answer, progression[:-1]
