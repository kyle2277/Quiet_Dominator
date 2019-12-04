import random
from collections import OrderedDict
from src.Board import Board
from src.Status import Status
from src.TreeNode import TreeNode
import copy


class AttributeManager:

    def __init__(self):
        pass

    def check_first(self, game, decisions, player):
        if len(game['com']) == len(game['user']):  # if true then com went first
            a = ('first',)
            return a
        else:
            a = ('second',)
            return a

    def check_list(self, game, decisions, player):
        for key, val in decisions.items():
            decision = tuple(game[player])
            if decision == key:
                return key
        return None

    def check_val(self, val, decision_val):  # check a string or int
        if val == decision_val:
            return decision_val
        else:
            return None

    def final(self, game, decisions, player):
        return 'final'

    def random(self, game):
        taken = game['com'] + game['user']
        value = str(random.randint(1, 9))
        while value in taken:
            value = str(random.randint(1, 9))
        return value

    attributes_dict = {
        0: ['first', 'bool', check_first],
        1: ['com', 'list', check_list],
        2: ['user', 'list', check_list],
        3: ['final', None, final],
        4: ['choose', None, None]
    }

    def train(self, file, tree, dimension):
        training_data = self.extract_data(file)
        for data in training_data:
            game = OrderedDict()
            game['com'] = data[0]
            game['user'] = data[1]
            self.trainer(game, tree, dimension)

    def extract_data(self, file):
        training_data = []
        with open(file, 'r') as f:
            for line in f:
                line = line.replace("\n", "")
                package = line.split("|")
                data = []
                for info in package:
                    info = str(info)
                    separated = info.split(",")
                    data.append(tuple(separated))
                training_data.append(data)
        return training_data

    def trainer(self, game, tree, dimension, board=None):
        if not board:
            board = self.game2board(self.clean(game), dimension)
        if board.check_win(board.board_list, dimension, 'com'):
            # print(board.board_list)
            # send to be added to tree
            self.dispatch(game, tree)
        elif board.check_win(board.board_list, dimension, 'user'):
            # switch com and user and then send to be added to tree
            new_game = OrderedDict()
            new_game['com'] = game['user']
            new_game['user'] = game['com']
            self.dispatch(new_game, tree)
            # send to be added to tree

    def clean(self, game):
        game_clean = copy.deepcopy(game)
        if len(game_clean['com']) > 0 and 'a' in game_clean['com'][0]:
            game_clean['com'][0] = game_clean['com'][0].replace('a', '')
        elif len(game_clean['user']) > 0 and 'a' in game_clean['user'][0]:
            game_clean['user'][0] = game_clean['user'][0].replace('a', '')
        return game_clean

    def game2board(self, game, dimension):
        cur_board = Board(dimension, numbered=False, preview=False)
        for com in game['com']:
            cur_board.board_list[int(com) - 1] = Status.com.value
        for user in game['user']:
            cur_board.board_list[int(user) - 1] = Status.user.value
        #  print completed board
        # cur_board.print_board()
        return cur_board

    def first(self, game):
        for key in game.keys():
            if 'a' in game[key][0]:
                return key
        return None

    def dispatch(self, game, tree):
        first = self.first(game)
        game_clean = self.clean(game)
        com = game_clean['com']
        user = game_clean['user']
        com_moves = []
        user_moves = []
        if first == 'com':  # com goes first
            print("com first")
            for i in range(len(com)-1):
                self.send(com_moves, user_moves, com[i], tree)
                # print(com_moves, "\n", user_moves, "\n", com[i])
                com_moves.append(com[i])
                user_moves.append(user[i])
                count = i
            # print(com_moves, "\n", user_moves, "\n", com[count+1])
            self.send(com_moves, user_moves, com[count + 1], tree)
        else:  # user goes first
            print("user first")
            for j in range(len(user)-1):
                user_moves.append(user[j])
                # print(com_moves, "\n", user_moves, "\n", com[j])
                self.send(com_moves, user_moves, com[j], tree)
                com_moves.append(com[j])

    def send(self, com_moves, user_moves, next_move, tree):
        game = OrderedDict()
        game['com'] = tuple(com_moves)
        game['user'] = tuple(user_moves)
        tree.overall_root = self.add_node(tree.overall_root, game, next_move)

    def add_node(self, root, game, next_move):
        traverse = root.decide(game, self.attributes_dict[root.attribute_number][0])
        if traverse in root.decisions:
            root.decisions[traverse] = self.add_node(root.decisions[traverse], game, next_move)
        elif self.attributes_dict[root.attribute_number][0] == 'first':
            new_node = TreeNode(root.attribute_number + 1, self)
            decision = traverse
            root.add_decision(decision, new_node)
            root.decisions[decision] = self.add_node(root.decisions[decision], game, next_move)
        elif self.attributes_dict[root.attribute_number][0] != 'final':
            new_node = TreeNode(root.attribute_number+1, self)
            key = self.attributes_dict[root.attribute_number][0]
            root.add_decision(game[key], new_node)
            root.decisions[game[key]] = self.add_node(root.decisions[game[key]], game, next_move)
        elif traverse == 'final':  # final branch, next node is the decision
            root.set_name(next_move)
        return root

