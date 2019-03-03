import os.path
from game import Game
from TreeNode import TreeNode
from AttributeManager import AttributeManager
from DecisionTree import DecisionTree
from Board import Board

DEFAULT_TREE = '3x3_3.txt'
CURRENT_TREE = ''
TREE = None


def __init__():
    manager = AttributeManager()
    # load default tree
    global TREE
    TREE = load_tree(DEFAULT_TREE, manager)
    # tree.print_tree()
    global CURRENT_TREE
    CURRENT_TREE = DEFAULT_TREE
    print("Default tree loaded.")
    main_menu(manager)


def load_tree(file, manager):
    f = open(file, 'r')
    global CURRENT_TREE
    CURRENT_TREE = file
    if not f.read():
        f.close()
        tree = DecisionTree(manager, file, True)
        # ready for training
    else:
        f.close()
        tree = DecisionTree(manager, file)
        tree.print_tree()
    return tree


def main_menu(manager):
    prompt = "vtec"
    while prompt != 'quit':
        prompt = input("ready")
        if prompt == 'help':
            print_help()
        elif prompt == 'quit':
            pass
        else:
            params = prompt.split(" ")
            if len(params) < 2:
                bad_input()
            else:
                global TREE
                TREE = run(params, manager)


def print_help():
    print("\ntrain <file> <game dimension>\t- train the algorithm with explicit game data of the given dimension")
    print("play <dimension of game> \t\t- play a tic-tac-toe game of specified dimension")
    print("play <dimension of game> -n \t- play a tic-tac-toe game of specified dimension with numbered squares")
    print("tree -l <tree file> \t\t\t- load a new decision tree/create new decision tree")
    print("tree -p \t\t\t\t\t\t- print the current decision tree")
    print("quit \t\t\t\t\t\t\t- exit the program\n")


def bad_input():
    print("input not recognized.\n")


def run(params, manager):
    command = params[0]
    options = params[1]
    if command == 'train':
        # train
        if len(params) != 3:
            bad_input()
        else:
            dimension = params[2]
            file = options
            if os.path.isfile(file):
                # todo training from main menu
                manager.train(file, TREE, dimension)
            else:
                print("file %s does not exists" % file)
            TREE.save_tree(CURRENT_TREE)
    elif command == 'play':
        # start game
        numbered = False
        if len(params) > 2:
            if params[2] == '-n':
                numbered = True
        dimension = options
        TREE.print_tree()
        Game(TREE, manager, dimension, numbered)
        TREE.save_tree(CURRENT_TREE)
        global TREE
        TREE = DecisionTree(manager, CURRENT_TREE)
    elif command == 'tree':
        # load or view
        if options == '-l':
            # load tree
            file = params[2]
            if os.path.isfile(file):
                new_tree = load_tree(file, manager)
                return new_tree
            else:
                print("file %s does not exist." % file)
        elif options == '-p':
            TREE.print_tree()
        else:
            print("tree command unrecognized")
            print("tree -l - load a new decision tree")
            print("tree -p - print the current decision tree\n")
        pass
    else:
        bad_input()
    return TREE


__init__()
