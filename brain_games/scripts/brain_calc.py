#!/usr/bin/env python
"""The main script of the package."""

from brain_games.games.general_logic import logic
from brain_games.games.calc_logic import expression_generator, action_to_do


def main():
    """Executiom of the entire programm."""

    logic(expression_generator, action_to_do)


if __name__ == '__main__':
    main()
