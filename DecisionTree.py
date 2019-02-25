import os.path
import sys
from TreeNode import TreeNode


class DecisionTree:

    def __init__(self, manager, f, new_tree=False):
        self.nodes = []
        self.manager = manager
        self.overall_root = TreeNode(0, manager)
        if new_tree:
            # todo ready for training
            pass
        else:
            # todo make method for building pre-existing tree
            self.build_tree(f)

    def build_tree(self, f):
        node_count = f.readline().replace("\n", "").split(',')
        self.overall_root = self.build_recur(self.overall_root, f, node_count, 1)

    def build_recur(self, root, f, node_count, layer):
        count = node_count.pop(0)
        if '0' not in count:
            for i in range(int(count)):
                decision = tuple(f.readline().replace("\n", "").split(','))
                new_node = TreeNode(layer, self.manager)
                root.add_decision(decision, self.build_recur(new_node, f, node_count, layer+1))
        else:  # end of the tree
            root.attribute_name = int(count)
        self.nodes.append(root)
        return root

    def print_tree(self):
        for i in range(len(self.manager.attributes_dict)):
            for node in self.nodes:
                if node.attribute_number == i:
                    print('|', node.attribute_name, " ", node.attribute_number, '| ', end="")
            print(end="\n")

        # for node in self.nodes:
        #     if node.attribute_number == 2:
        #         print(node.decisions)




