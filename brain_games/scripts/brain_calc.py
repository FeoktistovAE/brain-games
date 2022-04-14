#!/usr/bin/env python
"""The main script of the package."""

from brain_games.general_logic import gaming_engine
from brain_games.games import calc_logic


def main():
    """Executiom of the entire programm."""

    gaming_engine(calc_logic)


if __name__ == '__main__':
    main()
