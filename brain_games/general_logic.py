#!/usr/bin/env python
"""General logic module."""

import prompt


def logic(game_logic):
    """General logic for brain-games."""
    name = prompt.string('Welcome to the Brain Games!\nMay i have your name? ')
    print('Hello, {}!'.format(name))
    print(game_logic.PRINT_ACTION)
    score = 0
    FINAL_SCORE = 3

    while score < FINAL_SCORE:
        (res, print_expression) = game_logic.expressions()
        print(f'Question: {print_expression}')
        answer = prompt.string('Your answer: ')
        if answer == str(res):
            score += 1
            print('Correct!')
            if score == FINAL_SCORE:
                print(f'Congratulations, {name}!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{res}'.")
            print(f"Let's try again, {name}!'")
            break
