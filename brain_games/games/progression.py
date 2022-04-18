#!/usr/bin/env python
"""Must be imported by brain_progression.py."""
from random import randint, choice


DESCRIPTION = 'What number is missing in the progression?'


def get_expressions():
    consequence = ''
    first_value = randint(1, 70)
    distance = randint(2, 9)
    spread = randint(6, 11)
    counter = 0
    random_choice = choice(range(spread))
    for i in range(spread):
        if i == random_choice:
            answer = first_value + counter
            current_value = '..'
        else:
            current_value = str(first_value + counter,)
        consequence += current_value + ' '
        counter += distance
    return answer, consequence[:-1]
