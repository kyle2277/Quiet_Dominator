import os
import sys
import random
from TreeNode import TreeNode


class DecisionTree:

    def __init__(self, manager, f, new_tree=False):
        self.nodes = []
        self.manager = manager
        self.layers = len(self.manager.attributes_dict)
        self.overall_root = TreeNode(0, manager)
        if new_tree:
            # todo ready for training
            pass
        else:
            self.build_tree(f)

    def build_tree(self, f):
        node_count = f.readline().replace("\n", "").split(',')
        # print(node_count)
        self.overall_root = self.build_recur(self.overall_root, f, node_count, 1)

    def build_recur(self, root, f, node_count, layer):
        count = node_count.pop(0)
        if '@' not in count:
            for i in range(int(count)):
                decision = tuple(f.readline().replace("\n", "").split(','))
                new_node = TreeNode(layer, self.manager)
                root.add_decision(decision, self.build_recur(new_node, f, node_count, layer+1))
        else:  # end of the tree
            root.attribute_name = int(count.replace("@", ""))
        self.nodes.append(root)
        return root

    def save_tree(self, file):
        os.remove(file)
        f = open(file, 'w')
        child_count = []
        self.overall_root = self.save_recur(self.overall_root, child_count)
        add = ",".join(child_count) + "\n"
        dec_list = []
        self.overall_root = self.decisions_recur(self.overall_root, dec_list)
        add_dec = ""
        for dec in dec_list:
            add_dec = add_dec + ",".join(dec) + "\n"
        f.write(add)
        f.write(add_dec)
        f.close()

    def save_recur(self, root, child_count):
        if not root.num_children == 0:
            child_count.append(str(root.num_children))
            for node in root.decisions.values():
                node = self.save_recur(node, child_count)
        else:
            add = str(0) + str(root.attribute_name)
            child_count.append(add)
        return root

    def decisions_recur(self, root, dec_list):
        for dec, node in root.decisions.items():
            dec_list.append(dec)
            node = self.decisions_recur(node, dec_list)
        return root

    def make_decision(self, com, user, training=False):
        return self.make_decision_recur(com, user, self.overall_root, training)

    def make_decision_recur(self, com, user, root, training=False):
        if root.decisions:
            value_next = root.decide(com, user)
            if value_next:
                value = self.make_decision_recur(com, user, root.decisions[value_next], training)
            else:
                if training:
                    # todo manager object management
                    new_decision = TreeNode(root.attribute_number+1, root.manager)
                    root.add_decision(com, user, new_decision)
                    pass
                    #  if in training mode, add decisions from data
                else:
                    # todo com and user management
                    #  if in playing mode, generate random number that has not been chosen yet
                    taken = com + user
                    value = str(random.randint(1, 9))
                    while value in taken:
                        value = str(random.randint(1, 9))
            return value
        else:
            return root.attribute_name

    def add_decision(self, root, com, user, new_node):

    def print_tree(self):
        for i in range(self.layers):
            for node in self.nodes:
                if node.attribute_number == i:
                    print('|', node.attribute_name, " ", node.attribute_number, '| ', end="")
            print(end="\n")

        # for node in self.nodes:
        #     if node.attribute_number == 2:
        #         print(node.decisions)




