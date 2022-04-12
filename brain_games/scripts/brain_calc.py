#!/usr/bin/env python
"""The main script of the package."""

from brain_games.general_logic import logic
from brain_games.games import calc_logic


def main():
    """Executiom of the entire programm."""

    logic(calc_logic)


if __name__ == '__main__':
    main()
