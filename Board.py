from Status import Status
from three_by_three_rules import three_by_three_win


class Board:

    def __init__(self, dimension, numbered=True):
        self.board = []
        # self.board.append([Status.none.value] * dimension)
        count = 1
        for i in range(dimension):
            for j in range(dimension):
                if numbered:
                    self.board.append(count)
                else:
                    self.board.append(Status.none.value)
                count = count + 1
        self.dimension = dimension
        self.print_board()

    def move(self, move, player):
        if not self.check_valid_move(move):
            return False
        self.board[move-1] = Status[player].value
        squares = three_by_three_win(self.board, player)
        if squares:
            self.print_board(True, squares)
        else:
            self.print_board()
        return True

    def check_valid_move(self, move):
        return self.board[move-1] is not Status.com.value and self.board[move-1] is not Status.user.value

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
                    m2_add = "| " + str(self.board[count]) + " "
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
                        m2_add = "| " + str(self.board[count]) + " "
                    count = count + 1
                    m2.append(m2_add)
                m2.append("|")
                m2_draw = "".join(m2)
                print(m2_draw)
                self.draw_wall_bottom()

