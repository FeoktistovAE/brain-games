#!/usr/bin/env python
"""General logic module."""

import prompt

FINAL_SCORE = 3


def gaming_engine(game_logic):
    """General logic for brain-games."""
    name = prompt.string('Welcome to the Brain Games!\nMay i have your name? ')
    print('Hello, {}!'.format(name))
    print(game_logic.GAME_DESCRIBTION)

    for i in range(FINAL_SCORE):
        (res, print_expression) = game_logic.expressions()
        print(f'Question: {print_expression}')
        answer = prompt.string('Your answer: ')
        if answer == str(res):
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{res}'.")
            print(f"Let's try again, {name}!'")
            return
    print(f'Congratulations, {name}!')
