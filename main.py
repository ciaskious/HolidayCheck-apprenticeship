#!/usr/bin/env python
import os
import random

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

    # Puts the new value to the cell. If a move is repeated, the value is not replaced and the player loses his turn.

    def update_cell(self, position, player):
        if self.board[position] == " ":
            self.board[position] = player


if __name__ == "__main__":
    board = MyBoard()
    board.current_display()

    def refresh_screen():
        os.system("clear")

        board.current_display()

    # Main game loop

    while True:
        refresh_screen()
        x_move = int(raw_input("\nX) Please choose cell 1-9 . > "))

        board.update_cell(x_move-1, "X")

        refresh_screen()

        print("Computer choosing move...")
        o_move = int(random.randrange(9))
        board.update_cell(o_move, "O")

