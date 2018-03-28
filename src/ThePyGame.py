import sys
from board import *


def main(argv):
    num_players = 2
    board = Board(num_players)
    board.play()
    if not board.cards and len(board.winners) == num_players:
        print 'You Win!'
    else:
        print 'Game Over.'


if __name__ == "__main__":
    main(sys.argv)
