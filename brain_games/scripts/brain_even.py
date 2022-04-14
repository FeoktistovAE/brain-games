#!/usr/bin/env python

from brain_games.general_logic import gaming_engine
from brain_games.games import even_logic


def main():
    gaming_engine(even_logic)


if __name__ == '__main__':
    main()
