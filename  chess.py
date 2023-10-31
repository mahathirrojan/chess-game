import numpy as np
import time

class Game:
    def __init__(self):
        self.board = np.array([['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
                                ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
                                ['_', '_', '_', '_', '_', '_', '_', '_'],
                                ['_', '_', '_', '_', '_', '_', '_', '_'],
                                ['_', '_', '_', '_', '_', '_', '_', '_'],
                                ['_', '_', '_', '_', '_', '_', '_', '_'],
                                ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
                                ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']])
        self.game_continue = True
        self.winner = None

    def display_board(self):
        for row in self.board:
            print(' '.join(row))

    def play_game(self):
        self.display_board()
        while self.game_continue:
            start_row, start_col = map(int, input("Enter the starting row and column: ").split())
            end_row, end_col = map(int, input("Enter the ending row and column: ").split())

            if not self.is_valid_move(start_row, start_col, end_row, end_col):
                print("Invalid move. Try again.")
                continue

            self.make_move(start_row, start_col, end_row, end_col)
            self.display_board()

            self.check_for_winner()

            if self.winner:
                self.game_continue = False
                print(f"Game over. The winner is {self.winner}.")