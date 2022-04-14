#!/usr/bin/env python
"""Must be imported by brain_games.py."""

import prompt


def welcome_user():
    """Return user's welcome by using prompt.string package."""
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
