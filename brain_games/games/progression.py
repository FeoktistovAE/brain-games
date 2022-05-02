"""Must be imported by brain_progression.py."""
from random import randint


DESCRIPTION = 'What number is missing in the progression?'


def get_expression_and_result():
    first_value = randint(1, 70)
    step = randint(2, 9)
    progression_size = randint(6, 11)
    last_value = first_value + (progression_size - 1) * step
    random_index = randint(0, progression_size - 1)
    consequence = range(first_value, last_value + 1, step)
    progression = [str(item) for item in consequence]
    result = progression[random_index]
    progression[random_index] = '..'
    progression = (' '.join(progression))
    return progression, result
