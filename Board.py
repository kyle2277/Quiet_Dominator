from Status import Status
from three_by_three_rules import three_by_three_win


class Board:

    def __init__(self, dimension, numbered=True):
        self.board_list = []
        self.won = False
        # self.board.append([Status.none.value] * dimension)
        count = 1
        self.dimension = int(dimension)
        for i in range(self.dimension):
            for j in range(self.dimension):
                if numbered:
                    self.board_list.append(count)
                else:
                    self.board_list.append(Status.none.value)
                count = count + 1
        # self.print_board()

    def move(self, move, player):
        move = int(move)
        if not self.check_valid_move(move):
            return False
        self.board_list[move-1] = Status[player].value
        # print(self.board_list)
        squares = three_by_three_win(self.board_list, self.dimension, player)
        if squares:
            if 0 in squares:
                # print(squares)
                self.print_board()
                print("DRAW.")
            print("\n%s WON." % player.upper())
            self.print_board(True, squares)
            self.won = True
        else:
            self.print_board()
        return True

    def check_valid_move(self, move):
        return self.board_list[move-1] is not Status.com.value and self.board_list[move-1] is not Status.user.value

    def draw_walls(self):
        wall = ["|   "] * self.dimension
        wall.append("|")
        draw_wall = "".join(wall)
        print(draw_wall)

    def draw_top(self):
        top = ["____"] * self.dimension
        top.append("_")
        draw_top = "".join(top)
        print(draw_top)

    def draw_wall_bottom(self):
        wall_bottom = ["|___"]*self.dimension
        wall_bottom.append("|")
        draw_wall_bottom = "".join(wall_bottom)
        print(draw_wall_bottom)

    def print_board(self, win=False, squares=None):
        if not win:
            print()
            self.draw_top()
            count = 0
            for i in range(self.dimension):
                self.draw_walls()
                m2 = []
                for j in range(self.dimension):
                    m2_add = "| " + str(self.board_list[count]) + " "
                    count = count + 1
                    m2.append(m2_add)
                m2.append("|")
                m2_draw = "".join(m2)
                print(m2_draw)
                self.draw_wall_bottom()
        else:
            #  win
            print()
            self.draw_top()
            count = 0
            for i in range(self.dimension):
                self.draw_walls()
                m2 = []
                for j in range(self.dimension):
                    if count+1 in squares:
                        m2_add = "| @ "
                    else:
                        m2_add = "| " + str(self.board_list[count]) + " "
                    count = count + 1
                    m2.append(m2_add)
                m2.append("|")
                m2_draw = "".join(m2)
                print(m2_draw)
                self.draw_wall_bottom()
        print()

    def check_win(self, board_list, dimension, player):
        return three_by_three_win(board_list, dimension, player)

