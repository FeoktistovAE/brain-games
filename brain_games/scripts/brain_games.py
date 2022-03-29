#!/usr/bin/env python
"""The main script of the package."""
from brain_games.cli import welcome_user


def main():
    """Executiom of the entire programm."""
    print('Welcome to the Brain Games!')
    print(welcome_user())


if __name__ == '__main__':
    main()
