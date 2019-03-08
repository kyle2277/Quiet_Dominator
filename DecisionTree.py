import os
from TreeNode import TreeNode


class DecisionTree:

    def __init__(self, manager, file, new_tree=False):
        f = open(file, 'r')
        self.nodes = []
        self.manager = manager
        self.layers = len(self.manager.attributes_dict)
        self.overall_root = TreeNode(0, manager)
        if new_tree:
            print("ready for training.")
        else:
            self.build_tree(f)

    def build_tree(self, f):
        node_count = f.readline().replace("\n", "").split(',')
        self.overall_root = self.build_recur(self.overall_root, f, node_count)

    def build_recur(self, root, f, node_count):
        count = node_count.pop(0)
        if '@' not in count:
            for i in range(int(count)):
                decision = f.readline().replace("\n", "").split(',')
                # print(decision)
                if "_" in decision:
                    decision = ()
                else:
                    decision = tuple(decision)
                new_node = TreeNode(root.attribute_number + 1, self.manager)
                root.add_decision(decision, self.build_recur(new_node, f, node_count))
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
        dec_list = self.decisions_recur(self.overall_root, dec_list)
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
            add = str("@") + str(root.attribute_name)
            child_count.append(add)
        return root

    def decisions_recur(self, root, dec_list):
        for dec, node in root.decisions.items():
            if dec == ():
                empty = ("_",)
                dec_list.append(empty)
            else:
                dec_list.append(dec)
            dec_list = self.decisions_recur(node, dec_list)
        return dec_list

    def make_decision(self, game):
        return self.make_decision_recur(game, self.overall_root)

    def make_decision_recur(self, game, root):
        if root.decisions or root.attribute_number < 3:
            player = root.attribute_name
            value_next = root.decide(game, player)
            if value_next in root.decisions:
                value = self.make_decision_recur(game, root.decisions[value_next])
            else:
                #  if in playing mode, generate random number that has not been chosen yet
                print("random")
                value = self.manager.random(game)
            return value
        else:
            return root.attribute_name

    def print_tree(self):
        for i in range(self.layers):
            for node in self.nodes:
                if node.attribute_number == i:
                    print('|', node.attribute_name, " ", node.attribute_number, '| ', end="")
            print(end="\n")
