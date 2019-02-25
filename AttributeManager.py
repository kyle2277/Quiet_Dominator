class AttributeManager:

    def __init__(self):
        pass

    def check_first(self, com_moves, user_moves, decisions):
        if len(com_moves) == len(user_moves):  # if true then com went first
            a = ['first']
            return tuple(a)
        else:
            a = ['second']
            return tuple(a)

    def check_list(self, com_moves, user_moves, decisions):
        for key, val in decisions.items():
            if com_moves == key:
                return key
        return None

    def check_val(self, val, decision_val):  # check a string or int
        if val == decision_val:
            return decision_val
        else:
            return None

    # TODO write a method to check if won or lost

    attributes_dict = {
        0: ['who went first', 'bool', check_first],
        1: ['com squares', 'list', check_list],
        2: ['user squares', 'list', check_list],
        3: ['final', None, None]
    }

    def train(self, file, tree):
        training_data = self.extract_data(file)
        for data in training_data:
            pass

    def extract_data(self, file):
        training_data = []
        with open(file, 'r') as f:
            for line in f:
                line= line.replace("\n", "")
                package = line.split("|")
                data = []
                for info in package:
                    info = str(info)
                    separated = info.split(",")
                    data.append(tuple(separated))
                training_data.append(data)
        return training_data
