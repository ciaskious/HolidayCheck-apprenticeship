#!/usr/bin/env python
import os
import random
import time


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

    # Rules for a smart computer opponent

    def smart_player(self, player):
        # start from center - if still available
        if self.board[4] == " ":
            self.update_cell(4, player)
        else:
            # Random move for computer
            for pos in range(0, 9):
                if self.board[pos] == " ":
                    self.update_cell(pos, player)
                    break

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

    # Check if game's a tie

    def draw_game(self):
        used_moves = 0
        for pos in self.board:
            if pos != " ":
                used_moves += 1
        if used_moves == 9:
            return True
        else:
            return False


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

        # Check if Player X has the winning move
        if board.check_win("X"):
            print("\nHurray! You win <3 \n")

            play_again = raw_input("Would you like to play again? (y/N) > ")

            while play_again not in ("y", "N"):
                play_again = raw_input("Oops! Didn't get that... Would you like to play again? (y/N) > ")

            if play_again == "y":
                board.replay()
                continue
            else:
                break

        # Check if a draw occurs after Player X

        if board.draw_game():
            print("\nNo Losers, no winners!\n")

            play_again = raw_input("Wanna try again? (y/N) > ")

            while play_again not in ("y", "N"):
                play_again = raw_input("Oops! Didn't get that... Would you like to play again? (y/N) > ")

            if play_again == "y":
                board.replay()
                continue
            else:
                break

        # Delay computer's next move for 2 sec

        print("\nComputer choosing move... \n")


        # o_move = int(random.randrange(9))

        time.sleep(2)
        board.smart_player("O")

        # board.update_cell(o_move, "O")

        refresh_screen()

        # Check if Player O has the winning move

        if board.check_win("O"):
            print("\nComputer wins... But you can do better! \n")

            play_again = raw_input("Would you like to play again? (y/N) > ")

            while play_again not in ("y", "N"):
                play_again = raw_input("Oops! Didn't get that... Would you like to play again? (y/N) > ")

            if play_again == "y":
                board.replay()
                continue
            else:
                break

        # Check if a draw occurs after Player O

        if board.draw_game():
            print("\nNo Losers, no winners!\n")

            play_again = raw_input("Wanna try again? (y/N) > ")

            while play_again not in ("y", "N"):
                play_again = raw_input("Oops! Didn't get that... Would you like to play again? (y/N) > ")

            if play_again == "y":
                board.replay()
                continue
            else:
                break