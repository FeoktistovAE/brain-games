"""Must be imported by brain_progression.py."""
from random import randint, choice


DESCRIPTION = 'What number is missing in the progression?'


def get_data():
    first_value = randint(1, 70)
    step = randint(2, 9)
    spread = randint(6, 11)
    last_value = first_value + (spread - 1) * step
    random_choice = choice(range(spread - 1))
    consequence = range(first_value, last_value, step)
    progression = [str(item) for item in consequence]
    answer = int(progression[random_choice])
    progression[random_choice] = '..'
    progression = (' '.join(progression))
    return answer, progression
