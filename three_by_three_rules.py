from Status import Status


def three_by_three_win(board, player):
    squares = []
    check = []
    for x in board:
        check.append(board.index(x))
    for num in check:
        squares = check_horiz(num, player, board)
        if squares:
            return squares
        squares = check_vert(num, player, board)
        if squares:
            return squares
        if num == 1 or num == 3 or num == 5 or num == 7 or num == 9:
            squares = check_diag(num, player, board)
            if squares:
                return squares
    return None


def check_horiz(num, player, board):
    squares = []
    if num < 4:
        look = [1, 2, 3]
    elif num < 9:
        look = [4, 5, 6]
    else:
        look = [7, 8, 9]
    for i in look:
        if not board[i-1] == Status[player].value:
            return None
    return look


def check_vert(num, player, board):
    squares = []
    if num == 1 or num == 4 or num == 7:
        look = [1, 4, 7]
    elif num == 2 or num == 5 or num == 8:
        look = [2, 5, 8]
    else:
        look = [3, 6, 9]
    for i in look:
        if not board[i-1] == Status[player].value:
            return None
    return look


def check_diag(num, player, board):
    squares = []
    if num == 1 or num == 9:
        look = [1, 5, 9]
    else:
        look = [3, 5, 7]
    for i in look:
        if not board[i-1] == Status[player].value:
            return None
    return look
