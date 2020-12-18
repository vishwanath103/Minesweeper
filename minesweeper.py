import random

# board object to represent the minesweeper game
class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        # create the board
        self.board = self.make_new_board()
        self.assign_values_to_board()

        # intialize a set to keep track of which locations we have unconvered
        # save (row,col) tuples into this set
        self.dug = set()

    def make_new_board(self):
        # construct a list of list to represent board

        # generate a new board
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]

        # plant the bombs
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = rando,.randint(0, self.dim_size ** 2 -1)
            row = loc // self.dim_size
            col = loc % self.dim_size

            if board[row][col] == '*':
                continue

            board[row][col] = '*'
            bombs_planted += 1
        return board

    def assign_values_to_board(self):
        # assign a value 0-8 for all the empty spaces
        # which represents how many neighbouring bombs there are
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                    continue
                self.board[r][c] = self.get_num_neighboring_bombs(r,c)

    def get_num_neighboring_bombs(self, row, col):


# play the game
def play(dim_size=10, num_bombs=10):
    # step 1: create the board and plant the bombs
    # step 2: show user the board and ask where they want to dig
    # step 3a: if location is a bomb, show game over message
    # step 3b: if location is not a bomb, dig recursively until each square is atleast next to a bomb
    # step 4: repeat steps 2 and 3 until there are no more places to dig --> Victory
