"""General logic module."""

import prompt

ROUNDS = 3


def start(game):
    """General logic for brain-games."""
    name = prompt.string('Welcome to the Brain Games!\nMay i have your name? ')
    print('Hello, {}!'.format(name))
    print(game.DESCRIPTION)

    for round in range(ROUNDS):
        (result, expression) = game.get_data()
        print(f'Question: {expression}')
        answer = prompt.string('Your answer: ')
        if answer == str(result):
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. ", end='')
            print(f"Correct answer was '{result}'.")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
