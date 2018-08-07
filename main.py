#!/usr/bin/env python
import os


class MyBoard():
    os.system('clear')

    # Create board

    def __init__(self):
        self.board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    def current_display(self):
        print(" %s   | %s | %s " % (self.board[0], self.board[1], self.board[2]))
        print("---------------")
        print(" %s   | %s | %s " % (self.board[3], self.board[4], self.board[5]))
        print("---------------")
        print(" %s   | %s | %s " % (self.board[6], self.board[7], self.board[8]))


if __name__ == "__main__":
    board = MyBoard()
    board.current_display()
