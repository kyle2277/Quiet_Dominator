class TreeNode:

    def __init__(self, attribute_number, manager):
        # print(attribute_number)
        self.decisions = {}
        self.num_children = 0
        self.attribute_number = attribute_number
        self.attribute_name = manager.attributes_dict[attribute_number][0]
        self.decision_type = manager.attributes_dict[attribute_number][1]
        self.func_check = manager.attributes_dict[attribute_number][2]

    def add_decision(self, decision, next_node):
        self.decisions[decision] = next_node

    def make_decision(self):
        self.func_check(self.decisions)

    def add_decision(self, decision, node):
        self.decisions[decision] = node
