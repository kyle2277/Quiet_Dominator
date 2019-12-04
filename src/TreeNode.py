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

    def add_decision(self, decision, new_node):
        self.decisions[decision] = new_node
        self.num_children = len(self.decisions)

    def decide(self, game, player):
        return self.func_check(self.manager, game=game, decisions=self.decisions, player=player)

    def set_name(self, name):
        self.attribute_name = name
