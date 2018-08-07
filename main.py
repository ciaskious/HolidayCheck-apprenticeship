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

    # Reset the game

    def replay(self):
        self.board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    # Puts the new value to the cell. If a move is repeated, the value is not replaced and the player loses his turn.

    def update_cell(self, position, player):
        if self.board[position] == " ":
            self.board[position] = player

    # Get all moves a player has done so that we can find the winner

    def get_moves(self, player):
        moves = []
        for i in range(0, len(self.board)):
            if self.board[i] == player:
                moves.append(i)
        return moves

    # Search for a winning combination of moves on the board

    def check_win(self, player):
        winning_combos = ([0, 1, 2], [3, 4, 5], [6, 7, 8],
                          [0, 3, 6], [1, 4, 7], [2, 5, 8],
                          [0, 4, 8], [2, 4, 6])

        positions = self.get_moves(player)
        for combo in winning_combos:
            win = True
            for pos in combo:
                if pos not in positions:
                    win = False
            if win:
                return player


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

        if board.check_win("X"):
            print("\n=Hurray! You win <3 \n")

            play_again = raw_input("Would you like to play again? (y/N) > ")

            while play_again not in ("y", "N"):
                play_again = raw_input("Oops! Didn't get that... Would you like to play again? (y/N) > ")

            if play_again == "y":
                board.replay()
                continue
            else:
                break

        print("Computer choosing move...")
        o_move = int(random.randrange(9))
        board.update_cell(o_move, "O")

