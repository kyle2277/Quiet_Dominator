import os
from TreeNode import TreeNode
from AttributeManager import AttributeManager
from DecisionTree import DecisionTree
from Board import Board


def __init__():
    manager = AttributeManager()
    f = open('3x3_2.txt', 'r')
    if not f.read():
        tree = DecisionTree(manager, True)
    else:
        f.close()
        f = open('3x3_2.txt', 'r')
        tree = DecisionTree(manager, f)
        tree.print_tree()
        # tree.save_tree('3x3.txt')
        # board = Board(3, False)
        # board.move(2, 'com')
        # board.move(7, 'user')
        # board.move(9, 'com')
        # board.move(5, 'user')
        # board.move(3, 'com')
        # board.move(1, 'user')
        print(tree.make_decision(("1", "2"), ("3", "4")))
        manager.train('training.txt', tree)


__init__()
