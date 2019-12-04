import os
import random
import time
from collections import OrderedDict
from src.AttributeManager import AttributeManager

manager = AttributeManager()
dimensions = 3
gen_num = 10

# Todo COMMENT EVERYTHING


def main():
    global gen_num
    file = input("Enter name for new file: ")
    file = check_txt(file)
    while os.path.isfile(file):
        print("File %s already exists." % file)
        ask_overwrite = input("Would you like to overwrite this file? [y/n]")
        if ask_overwrite == 'y':
            break
        file = input("Enter name for new file: ")
        file = check_txt(file)
    f = open(file, 'w')
    global gen_num
    get_num = "Motronic"
    while get_num:
        get_num = input("How many games do you want to generate?\n[enter] Default = %s: " % gen_num)
        try:
            if isinstance(int(get_num), int):
                gen_num = int(get_num)
                get_num = None
        except ValueError:
            pass
    start = time.process_time()
    f.write(generate_data())
    elapsed = str(time.process_time() - start)
    print("%s games generated in %s seconds." % (gen_num, elapsed))


def check_txt(file):
    return file if '.txt' in file else file + '.txt'


def generate_data():
    global gen_num
    output = ''
    for x in range(gen_num):
        output = output + generate_game()
    return output


def generate_game():
    game = generate_single_game()
    com = ",".join(game['com'])
    user = ",".join(game['user'])
    game_data = com + "|" + user + "\n"
    return game_data


def generate_single_game():
    global manager
    p1 = []
    p2 = []
    o = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(4):
        rand = random.randint(1, len(o))
        if len(p1) == 0:
            append = str(o[rand-1]) + "a"
            p1.append(append)
        else:
            p1.append(str(o[rand-1]))
        o.pop(rand-1)
        check = check_win(p1, p2)
        if check:
            return check
        rand = random.randint(1, len(o))
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
        # board.print_board(win=True, squares=squares_com)
        return game
    elif squares_user:
        # board.print_board(win=True, squares=squares_user)
        return array2game(p1, p2, switch=True)
    else:
        return None


main()

