#!/usr/bin/env python
"""General logic module."""

import prompt


def logic(expression_generator, action_to_do):
    """Print user's welcome by using prompt.string package."""
    name = prompt.string('Welcome to the Brain Games!\nMay i have your name? ')
    print('Hello, {}!'.format(name))
    print(action_to_do)
    score = 0

    while score < 3:
        (res, print_expression) = expression_generator()
        print(f'Question: {print_expression}')
        answer = prompt.string('Your answer: ')
        if answer == str(res):
            score += 1
            print('Correct!')
            if score == 3:
                print(f'Congratulations, {name}!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{res}'.")
            print(f"Let's try again, {name}!'")
            break
