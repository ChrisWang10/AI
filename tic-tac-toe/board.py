"""
alpha-beta pruning for min-max game
"""
import numpy as np


class GameBoard:
    def __init__(self, board_size):
        self.board_size = board_size
        self.board = [' '] * (self.board_size * self.board_size)

    def __repr__(self):
        """
        :return: return a string representation of the board
        """
        ret = '\n'
        for i in range(len(self.board)):
            if self.board[i] == ' ':
                ret += str(i)
            else:
                ret += self.board[i]
            if (i+1)%self.board_size == 0:
                ret += '\n'
        ret += '\n'
        return ret




def main():
    gb = GameBoard(board_size=3)


if __name__ == '__main__':
    main()
