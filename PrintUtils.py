def print_board(board):
    '''
    This method expects a chess board containing a numpy array of length 64.
    It then prints it in a human readable way.
    '''
    print('---------------------------------')
    rank_header = '|  || A| B| C| D| E| F| G| H||  |'
    print(rank_header)
    lines = []
    for i in range(0,8):
        rank = i+1
        cur_line = f'| {rank}||'
        for j in range(0,8):
            cur_cell = board.board[i*8 + j]
            if len(str(cur_cell)) == 1:
                cur_line += f' {cur_cell}|'
            elif len(str(cur_cell)) == 2:
                cur_line += f'{cur_cell}|'

        cur_line += f'| {rank}|'

        lines.append(cur_line)

    i = 7
    while i >= 0:
        print(lines[i])
        i -= 1

    print(rank_header)
    print('---------------------------------')
