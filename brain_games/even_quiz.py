#!/usr/bin/env python
"""Must be imported by brain_even.py."""

import prompt
from random import randint


def even_game():
    """Print user's welcome by using prompt.string package."""
    name = prompt.string('Welcome to the Brain Games!\nMay i have your name? ')
    print('Hello, {}!'.format(name))
    print('Answer "yes" if the number is even, otherwise answer "no"')
    result = True
    score = 0
    while result is True:
        random_number = randint(1, 100)
        print(f'Question: {random_number}')
        answer = prompt.string('Your answer: ')
        rest = random_number % 2
        if rest == 0 and answer == 'yes' or rest != 0 and answer == 'no':
            score += 1
            print('Correct!')
            if score == 3:
                result = False
                print(f'Congratulations, {name}!')
        else:
            result = False
            print("'yes' is wrong answer ;(. Correct answer was 'no'.")
            print(f"Let's try again, {name}!'")
