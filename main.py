import os.path
from TreeNode import TreeNode
from AttributeManager import AttributeManager
from DecisionTree import DecisionTree
from Board import Board

DEFAULT_TREE = '3x3_2.txt'


def __init__():
    manager = AttributeManager()
    load = input("Load default decision tree? [y/n]")
    if load == 'y':  # load default tree
        tree = load_tree(DEFAULT_TREE, manager)
    else:  # load user specified tree
        user_load = input("Please enter the file name of the tree to load:")
        tree = load_tree(user_load, manager)
    main_menu(tree, manager)


def load_tree(file, manager):
    f = open(file, 'r')
    if not f.read():
        f.close()
        tree = DecisionTree(manager, file, True)
        # ready for training
    else:
        f.close()
        tree = DecisionTree(manager, file)
        tree.print_tree()
        # board = Board(3, False)
        # board.move(2, 'com')
        # board.move(7, 'user')
        # board.move(9, 'com')
        # board.move(5, 'user')
        # board.move(3, 'com')
        # board.move(1, 'user')
        # print(tree.make_decision({'com': ("1", "2"), 'user': ("3", "4")}))
        # manager.train('training.txt', tree)
        # tree.save_tree('3x3_2.txt')
        # f.close()
        # f = open('3x3_2.txt', 'r')
        # tree2 = DecisionTree(manager, f)
        # tree2.print_tree()
    return tree


def main_menu(tree, manager):
    prompt = "vtec"
    while prompt != 'quit':
        prompt = input("ready")
        if prompt == 'help':
            print_help()
        elif prompt == 'quit':
            pass
        else:
            params = prompt.split(" ")
            if len(params) != 2:
                bad_input()
            else:
                tree = run(params, tree, manager)


def print_help():
    print("\ntrain <training file> - train the algorithm with explicit game data")
    print("play <dimension of game> - play a tic-tac-toe game of specified dimension")
    print("tree -l - load a new decision tree")
    print("tree -p - print the current decision tree")
    print("quit - exit the program\n")


def bad_input():
    print("input not recognized.\n")


def run(params, tree, manager):
    command = params[0]
    options = params[1]
    if command == 'train':
        # train
        file = options
        if os.path.isfile(file):
            # train
            pass
        else:
            print("file %s does not exists" % file)
        pass
    elif command == 'play':
        # start game
        dimension = options
        pass
    elif command == 'tree':
        # load or view
        if options == '-l':
            # load tree
            file = input("Please enter the file name of the tree to load:")
            if os.path.isfile(file):
                new_tree = load_tree(file, manager)
                return new_tree
            else:
                print("file %s does not exist." % file)
        elif options == '-p':
            tree.print_tree()
        else:
            print("tree command unrecognized")
            print("tree -l - load a new decision tree")
            print("tree -p - print the current decision tree\n")
        pass
    else:
        bad_input()
    return tree


__init__()
