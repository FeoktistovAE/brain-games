#!/usr/bin/env python
"""The main script of the package."""

from brain_games.game_engine import start
from brain_games.games import calc


def main():
    """Executiom of the entire programm."""

    start(calc)


if __name__ == '__main__':
    main()
