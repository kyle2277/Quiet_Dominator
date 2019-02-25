import os
from TreeNode import TreeNode
from AttributeManager import AttributeManager
from DecisionTree import DecisionTree


def __init__():
    manager = AttributeManager()
    f = open('3x3.txt', 'r')
    if not f.read():
        tree = DecisionTree(manager, True)
    else:
        f.close()
        f = open('3x3.txt', 'r')
        tree = DecisionTree(manager, f)
        tree.print_tree()


__init__()
