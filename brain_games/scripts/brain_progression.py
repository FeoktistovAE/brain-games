#!/usr/bin/env python

from brain_games.games.general_logic import logic
from brain_games.games.progr_logic import expression_generator, action_to_do


def main():
    logic(expression_generator, action_to_do)


if __name__ == '__main__':
    main()
