import string
import itertools


class TicTacToe:
    def __init__(self):
        self.wins = None
        self.move = None
        self.turn = 1
        self.accepted = ['X', 'O', '_', ' ']
        self.start = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.playing_grid = [self.start[:3], self.start[3:6], self.start[6:9]]

    def game_board(self):
        self.game_board = [["---------"],
                           ['| ', " ".join(self.playing_grid[0]), ' |'],
                           ['| ', " ".join(self.playing_grid[1]), ' |'],
                           ['| ', " ".join(self.playing_grid[2]), ' |'],
                           ["---------"]
                           ]
        for row in self.game_board:
            print("".join(row))

    def game_state(self):
        if 'XXX' in self.wins and 'OOO' in self.wins:
            print('Impossible')
        elif abs(self.start.count('X') - self.start.count('O')) > 1:
            print('Impossible')
        elif 'XXX' in self.wins:
            print('X wins')
            exit()
        elif 'OOO' in self.wins:
            print('O wins')
            exit()
        elif self.start.count(' ') == 0:
            print('Draw')
            exit()

    def moves(self):
        self.game_board()
        while True:
            self.turn += 1
            self.start[0] = self.playing_grid[0][0]
            self.start[1] = self.playing_grid[0][1]
            self.start[2] = self.playing_grid[0][2]
            self.start[3] = self.playing_grid[1][0]
            self.start[4] = self.playing_grid[1][1]
            self.start[5] = self.playing_grid[1][2]
            self.start[6] = self.playing_grid[2][0]
            self.start[7] = self.playing_grid[2][1]
            self.start[8] = self.playing_grid[2][2]
            self.wins = [''.join(self.start[:3]), ''.join(self.start[3:6]), ''.join(self.start[6:9]),
                         ''.join(self.start[:7:3]), ''.join(self.start[1:8:3]), ''.join(self.start[2:9:3]),
                         ''.join(self.start[:9:4]), ''.join(self.start[2:7:2])]
            self.game_state()
            self.move = input('Enter the coordinates: ').split()
            if any(coord not in string.digits for coord in self.move):
                print("You should enter numbers!")
                continue
            int_coord = [int(coord) for coord in self.move]
            if any(coord < 1 or coord > 3 for coord in int_coord):
                print("Coordinates should be from 1 to 3!")
                continue
            grid_coord = [(int_coord[0] - 1), int_coord[1] - 1]
            if self.playing_grid[grid_coord[0]][grid_coord[1]] != ' ':
                print("This cell is occupied! Choose another one!")
                continue
            if self.turn % 2 == 0:
                self.playing_grid[grid_coord[0]][grid_coord[1]] = "X"
                TicTacToe.game_board(new_game)
                continue
            if self.turn % 2 != 0:
                self.playing_grid[grid_coord[0]][grid_coord[1]] = "O"
                TicTacToe.game_board(new_game)
                continue
            if " " not in self.playing_grid:
                print("Draw")
                break


new_game = TicTacToe()
new_game.moves()
