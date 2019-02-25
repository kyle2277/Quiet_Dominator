class AttributeManager:

    def __init__(self):
        pass

    def check_first(self, com_moves, user_moves):
        return len(com_moves) == len(user_moves)  # if true then com went first

    def check_list(self, list_moves, decision):
        return list_moves == decision

    def check_val(self, val, decision_val):  # check a string or int
        return val == decision_val

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
                    data.append(separated)
                training_data.append(data)
        return training_data
