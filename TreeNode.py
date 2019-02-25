from collections import OrderedDict


class TreeNode:

    def __init__(self, attribute_number, manager):
        self.manager = manager
        self.decisions = OrderedDict()
        self.num_children = 0
        self.attribute_number = attribute_number
        self.attribute_name = manager.attributes_dict[attribute_number][0]
        self.decision_type = manager.attributes_dict[attribute_number][1]
        self.func_check = manager.attributes_dict[attribute_number][2]

    def add_decision(self, decision, next_node):
        self.decisions[decision] = next_node

    def decide(self, com, user):
        return self.func_check(self.manager, com_moves=com, user_moves=user, decisions=self.decisions)

    def add_decision(self, decision, node):
        self.decisions[decision] = node
        self.num_children = len(self.decisions)
