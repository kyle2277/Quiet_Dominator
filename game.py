from Board import Board
from collections import OrderedDict
import random
import copy


class Game:

    def __init__(self, tree, manager, dimension, numbered):
        self.com_moves = []
        self.user_moves = []
        self.game = {
            'com': self.com_moves,
            'user': self.user_moves
        }
        self.tree = tree
        self.manager = manager
        self.dimension = dimension
        self.game_board = Board(dimension, numbered)
        fin_game = self.play()
        if self.game_board.won:
            manager.trainer(fin_game, tree, board=self.game_board, dimension=self.dimension)

    def play(self):
        functions = {
            'com': self.com_move,
            'user': self.user_move
        }
        first = self.choose_first()
        order = OrderedDict()
        order[first] = functions[first]
        if first == 'com':
            order['user'] = functions['user']
        else:
            order['com'] = functions['com']
        while not self.game_board.won:
            for player, func in order.items():
                player_move = func()
                if len(self.game['com']) == 0 and len(self.game['user']) == 0:
                    self.game[player].append(str(player_move) + 'a')
                else:
                    self.game[player].append(str(player_move))
                if self.game_board.won:
                    break
        return self.game

    def com_move(self):
        game_clean = copy.deepcopy(self.game)
        move = self.tree.make_decision(self.manager.clean(game_clean))
        self.game_board.move(move, 'com')
        return move

    def user_move(self):
        move = input("Enter a move:")
        if not self.game_board.move(move, 'user'):
            print("invalid move.")
            return self.user_move()
        return move

    def choose_first(self):
        print("would you like to go first?")
        print("y - yes")
        print("n - no")
        print("r - random")
        console = input()
        if console == 'y':
            return 'user'
        elif console == 'n':
            return 'com'
        elif console == 'r':
            rand = random.randint(0, 1)
            if rand == 0:
                return 'com'
            else:  # console == 1
                return 'user'
        else:
            return self.choose_first()