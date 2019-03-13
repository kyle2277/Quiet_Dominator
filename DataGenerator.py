import os
import random
from collections import  OrderedDict
from AttributeManager import AttributeManager

manager = AttributeManager()
dimensions = 3


def __init__():
    # todo write game generator
    # file = input("Enter name for new file: ")
    # while os.path.isfile(file):
    #     print("File %s already exists." % file)
    #     file = input("Enter name for new file: ")
    # f = open(file, 'w')
    # f.write(generate_data())
    generate_data()


def generate_data():
    generate_game()


def generate_game():
    game = generate_single_game()
    com = ",".join(game['com'])
    user = ",".join(game['user'])
    game_data = com + "|" + user
    print(game_data)



def generate_single_game():
    global manager
    p1 = []
    p2 = []
    o = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(4):
        print(o)
        rand = random.randint(1, len(o))
        print(rand)
        if len(p1) == 0:
            p1.append(str(o[rand-1])+'a')
        else:
            p1.append(str(o[rand-1]))
        o.pop(rand-1)
        check = check_win(p1, p2)
        if check:
            return check
        rand = random.randint(1, len(o))
        print(rand)
        p2.append(str(o[rand-1]))
        o.pop(rand-1)
        check = check_win(p1, p2)
        if check:
            return check
    p1.append(str(o[0]))
    o.pop(0)
    check = check_win(p1, p2)
    return check if check else generate_single_game()


def array2game(p1, p2, switch=False):
    game = OrderedDict()
    game['com'] = p1
    game['user'] = p2
    if not switch:
        return game
    else:
        new_game = OrderedDict()
        new_game['com'] = game['user']
        new_game['user'] = game['com']
        return new_game


def check_win(p1, p2):
    global dimensions
    game = array2game(p1, p2)
    board = manager.game2board(manager.clean(game), dimensions)
    squares_com = board.check_win(board.board_list, dimensions, 'com')
    squares_user = board.check_win(board.board_list, dimensions, 'user')
    if squares_com:
        board.print_board(win=True, squares=squares_com)
        return game
    elif squares_user:
        board.print_board(win=True, squares=squares_user)
        return array2game(p1, p2, switch=True)
    else:
        return None


__init__()

