#!/usr/bin/env python
"""General logic module."""

import prompt

ROUNDS = (1, 2, 3)


def start(game):
    """General logic for brain-games."""
    name = prompt.string('Welcome to the Brain Games!\nMay i have your name? ')
    print('Hello, {}!'.format(name))
    print(game.DESCRIPTION)

    for round in ROUNDS:
        (result, print_expression) = game.get_expressions()
        print(f'Question: {print_expression}')
        answer = prompt.string('Your answer: ')
        if answer == str(result):
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. ", end='')
            print(f"Correct answer was '{result}'.")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
