from lib import *
from math import floor
# Piece constants
EMPTY = 0

# Directions
TOP = 0
RIGHT = 1
LEFT = 2
BOTTOM = 3

class ChessBoard:

    def __init__(self):
        self.board = np.zeros((64),dtype=np.int8)
        self.board[0] = 1


    def move(self,from_cell,to_cell):
        # parse the cell values to indices
        from_index = self.parse_alg_not_2_index(from_cell)
        to_index = self.parse_alg_not_2_index(to_cell)

        if self.is_in_bounds(from_cell) and self.is_in_bounds(to_cell):
            self.board[to_index] = self.board[from_index]
            self.board[from_index] = EMPTY
            print(f'Successfully moved from {from_cell} to {to_cell}')

            return True
        else:
            print('One of the cells is not in bounds')
            return False



    def straight_line_movement(self,from_cell,steps:int,direction):
        from_index = self.parse_alg_not_2_index(from_cell)

        if direction == TOP:
            to_index = from_index + (8*steps)
        elif direction == BOTTOM:
            to_index = from_index - (8*steps)
        elif direction == RIGHT:
            to_index = from_index + steps
        elif direction == LEFT:
            to_index = from_index - steps


        return self.move(from_cell,self.parse_index_2_alg_not(to_index))


    def diagonal_move(self,from_cell,steps:int,vertical_direction,horizontal_direction):
        from_index = self.parse_alg_not_2_index(from_cell)

        if vertical_direction == TOP:
            if horizontal_direction == RIGHT:
                # top-right
                to_index = from_index + (8*steps) + steps
            elif horizontal_direction == LEFT:
                # top-left
                to_index = from_index + (8*steps) - steps
        elif vertical_direction == BOTTOM:
            if horizontal_direction == RIGHT:
                # bottom-right
                to_index = from_index - (8*steps) + steps
            elif horizontal_direction == LEFT:
                # bottom-left
                to_index = from_index - (8*steps) - steps

        return self.move(from_cell,self.parse_index_2_alg_not(to_index))


    def knight_move(self,from_cell, direction1, direction2):
        from_index = self.parse_alg_not_2_index(from_cell)
        if direction1 == TOP:
            if direction2 == RIGHT:
                # top-right
                to_index = from_index + (2*8) + 1
            elif direction2 == LEFT:
                # top-left
                to_index = from_index + (2*8) - 1
        elif direction1 == BOTTOM:
            if direction2 == RIGHT:
                # bottom-right
                to_index = from_index - (2*8) + 1

            elif direction2 == LEFT:
                # bottom-left
                to_index = from_index - (2*8) - 1

        elif direction1 == RIGHT:
            if direction2 == TOP:
                # right-top
                to_index = from_index + 8 + 2

            elif direction2 == BOTTOM:
                # right-bottom
                to_index = from_index - 8 + 2

        elif direction1 == LEFT:
            if direction2 == TOP:
                # left-top
                to_index = from_index + 8 - 2

            elif direction2 == BOTTOM:
                # left-bottom
                to_index = from_index - 8 - 2

        return self.move(from_cell,self.parse_index_2_alg_not(to_index))


    def is_in_bounds(self,cell):
        index = self.parse_alg_not_2_index(cell)

        if index >= 0 and index <= 63:
            return True
        else:
            return False


    def parse_alg_not_2_index(self,algebraic_notation):
        file = ord(algebraic_notation[0]) - ord('A') # this shifts the file value between 0...7
        rank = int(algebraic_notation[1]) - 1 # this shifts the file value between 0...7

        index = file * 8 + rank

        return index


    def parse_index_2_alg_not(self,index):
        file = chr(ord('A') + floor(index/8)) # returns A ... H
        rank = (index % 8) + 1 # returns 1 ... 8

        algebraic_notation = file + f'{rank}'

        return algebraic_notation