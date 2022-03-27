#!/usr/bin/env python
def welcome_user():
    import prompt
    name = prompt.string('May i have your name? ')
    print(f'Hello, {name}!')
