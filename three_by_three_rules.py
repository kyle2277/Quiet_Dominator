from Status import Status


def three_by_three_win(board_list, dimension, player):
    check = []
    for count, x in enumerate(board_list):
        if x == Status[player].value:
            check.append(count+1)
    for num in check:
        squares = check_horiz(num, player, board_list)
        if squares:
            return squares
        squares = check_vert(num, player, board_list)
        if squares:
            return squares
        if num == 1 or num == 3 or num == 5 or num == 7 or num == 9:
            squares = check_diag(num, player, board_list)
            if squares:
                return squares
    # todo more sophisticated draw detection
    xs = board_list.count(Status.com.value)
    os = board_list.count(Status.user.value)
    total = xs + os
    if Status.none.value not in board_list and total == (int(dimension)*int(dimension)):
        print("DRAW")
        return [0]*3
    return None


def check_horiz(num, player, board_list):
    if num < 4:
        look = [1, 2, 3]
    elif num < 6:
        look = [4, 5, 6]
    else:
        look = [7, 8, 9]
    for i in look:
        if not board_list[i-1] == Status[player].value:
            return None
    return look


def check_vert(num, player, board_list):
    if num == 1 or num == 4 or num == 7:
        look = [1, 4, 7]
    elif num == 2 or num == 5 or num == 8:
        look = [2, 5, 8]
    else:
        look = [3, 6, 9]
    for i in look:
        if not board_list[i-1] == Status[player].value:
            return None
    return look


def check_diag(num, player, board_list):
    if num == 1 or num == 9:
        look = [1, 5, 9]
    else:
        look = [3, 5, 7]
    for i in look:
        if not board_list[i-1] == Status[player].value:
            return None
    return look
