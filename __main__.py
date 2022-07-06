from lib import *

if __name__ == '__main__':
    my_chess_board = ChessBoard()

    print_board(my_chess_board)

    my_chess_board.knight_move('A1',RIGHT,TOP)

    print_board(my_chess_board)