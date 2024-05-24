import numpy as np
import random
import math
import threading
import sys
import os


#CONST VALUES
weights = [
    [20, -3, 11, 8, 8, 11, -3, 20],
    [-3, -7, -4, 1, 1, -4, -7, -3],
    [11, -4, 8, 2, 2, 8, -4, 11],
    [8, 1, 2, -3, -3, 2, 1, 8],
    [8, 1, 2, -3, -3, 2, 1, 8],
    [11, -4, 8, 2, 2, 8, -4, 11],
    [-3, -7, -4, 1, 1, -4, -7, -3],
    [20, -3, 11, 8, 8, 11, -3, 20]
]

dirs = [
    [0, 1], [0, -1], [1, 0], [-1, 0],
    [1, 1], [1, -1], [-1, 1], [-1, -1]
]


#======

def deepcopy(obj):
    res = Game(obj.me, obj.board_size)
    res.board = np.array(obj.board.copy())
    res.freeCells = obj.freeCells.copy()
    return res


class Game:

    # player 1 - white, 0 - black
    def __init__(self, who_we_play_as, board_size=8):
        self.board = [[None] * board_size for _ in range(board_size)]
        self.board[3][3] = 1
        self.board[4][4] = 1
        self.board[3][4] = 0
        self.board[4][3] = 0
        self.corners = []
        self.corners.append((0, 0))
        self.corners.append((0, board_size - 1))
        self.corners.append((board_size - 1, 0))
        self.corners.append((board_size - 1, board_size - 1))
        self.board_size = board_size
        self.current_player = 0
        self.me = who_we_play_as
        self.opp = 1 - who_we_play_as
        self.freeCells = set()
        self.moves_list = []
        self.history = []
        self.fields = set()
        for i in range(board_size):
            for j in range(board_size):
                if (self.board[i][j] == None):
                    self.freeCells.add((i, j))
                    self.fields.add((i, j))

    def __str__(self):
        answer = ""
        for i in range(self.board_size):
            for j in range(self.board_size):
                if self.board[i][j] == None:
                    answer += "."
                elif self.board[i][j] == 0:
                    answer += "B"
                else:
                    answer += "W"
            answer += "\n"
        return answer

    def in_board(self, i, j):
        return i >= 0 and i < self.board_size and j >= 0 and j < self.board_size

    def valid_moves(self, player):
        res = []
        for (x, y) in self.fields:
            if any(self.can_beat(x, y, direction, player)
                   for direction in dirs):
                res.append((x, y))
        return res

    def can_beat(self, x, y, d, player):
        dx, dy = d
        x += dx
        y += dy
        cnt = 0
        while self.get(x, y) == 1 - player:
            x += dx
            y += dy
            cnt += 1
        return cnt > 0 and self.get(x, y) == player

    def get(self, x, y):
        if 0 <= x < self.board_size and 0 <= y < self.board_size:
            return self.board[y][x]
        return None

    def make_move(self, move, player):
        self.history.append([x[:] for x in self.board])
        self.moves_list.append(move)

        if move is None:
            return
        x, y = move
        x0, y0 = move
        self.board[y][x] = player
        self.fields -= set([move])
        for dx, dy in dirs:
            x, y = x0, y0
            to_beat = []
            x += dx
            y += dy
            while self.get(x, y) == 1 - player:
                to_beat.append((x, y))
                x += dx
                y += dy
            if self.get(x, y) == player:
                for (nx, ny) in to_beat:
                    self.board[ny][nx] = player

    def score(self):
        score = 0
        for i in range(self.board_size):
            for j in range(self.board_size):
                if self.board[i][j] == 0:
                    score += 1
                elif self.board[i][j] == 1:
                    score -= 1
        return score

    def is_end(self):
        if not self.freeCells:
            return True
        if len(self.moves_list) < 2:
            return False
        return self.moves_list[-1] == self.moves_list[-2] == None

    def random_move(self, color):
        ms = self.valid_moves(color)
        if ms:
            return random.choice(ms)
        return [None]

    def coin_parity(self):
        my_tiles = 0
        opp_tiles = 0
        for i in range(self.board_size):
            for j in range(self.board_size):
                if self.board[i][j] == self.me:
                    my_tiles += 1
                elif self.board[i][j] == self.opp:
                    opp_tiles += 1
        # return 100 * (my_tiles - opp_tiles) / (my_tiles + opp_tiles)
        if my_tiles > opp_tiles:
            return (100.0 * my_tiles) / (my_tiles + opp_tiles)
        elif my_tiles < opp_tiles:
            return -(100.0 * opp_tiles) / (my_tiles + opp_tiles)
        return 0

    def cornersCalculate(self):
        my_tiles = 0
        opp_tiles = 0
        for corner in self.corners:
            if self.board[corner[0]][corner[1]] == self.me:
                my_tiles += 1
            elif self.board[corner[0]][corner[1]] == self.opp:
                opp_tiles += 1
        return 25 * (my_tiles - opp_tiles)

    def nextToCorners(self):
        my_tiles = 0
        opp_tiles = 0
        if self.board[0][0] == None:
            if self.board[0][1] == self.me:
                my_tiles += 3
            elif self.board[0][1] == self.opp:
                opp_tiles += 3
            if self.board[1][1] == self.me:
                my_tiles += 2
            elif self.board[1][1] == self.opp:
                opp_tiles += 2
            if self.board[1][0] == self.me:
                my_tiles += 1
            elif self.board[1][0] == self.opp:
                opp_tiles += 1
        if self.board[0][self.board_size - 1] == None:
            if self.board[0][self.board_size - 2] == self.me:
                my_tiles += 3
            elif self.board[0][self.board_size - 2] == self.opp:
                opp_tiles += 3
            if self.board[1][self.board_size - 2] == self.me:
                my_tiles += 2
            elif self.board[1][self.board_size - 2] == self.opp:
                opp_tiles += 2
            if self.board[1][self.board_size - 1] == self.me:
                my_tiles += 1
            elif self.board[1][self.board_size - 1] == self.opp:
                opp_tiles += 1
        if self.board[self.board_size - 1][0] == None:
            if self.board[self.board_size - 1][1] == self.me:
                my_tiles += 3
            elif self.board[self.board_size - 1][1] == self.opp:
                opp_tiles += 3
            if self.board[self.board_size - 2][1] == self.me:
                my_tiles += 2
            elif self.board[self.board_size - 2][1] == self.opp:
                opp_tiles += 2
            if self.board[self.board_size - 2][0] == self.me:
                my_tiles += 1
            elif self.board[self.board_size - 2][0] == self.opp:
                opp_tiles += 1
        if self.board[self.board_size - 1][self.board_size - 1] == None:
            if self.board[self.board_size - 1][self.board_size - 2] == self.me:
                my_tiles += 3
            elif self.board[self.board_size - 1][self.board_size - 2] == self.opp:
                opp_tiles += 3
            if self.board[self.board_size - 2][self.board_size - 2] == self.me:
                my_tiles += 2
            elif self.board[self.board_size - 2][self.board_size - 2] == self.opp:
                opp_tiles += 2
            if self.board[self.board_size - 2][self.board_size - 1] == self.me:
                my_tiles += 1
            elif self.board[self.board_size - 2][self.board_size - 1] == self.opp:
                opp_tiles += 1

        return -12.5 * (my_tiles - opp_tiles)

    def mobility(self):
        my_tiles = len(self.valid_moves(self.me))
        opp_tiles = len(self.valid_moves(self.opp))
        if my_tiles > opp_tiles:
            return (100.0 * my_tiles) / (my_tiles + opp_tiles)
        elif my_tiles < opp_tiles:
            return -(100.0 * opp_tiles) / (my_tiles + opp_tiles)
        return 0

    def heuristic(self, amount):
        my_tiles = 0
        opp_tiles = 0

        p, c, l, m, d = 0, 0, 0, 0, 0
        my_cord = []
        opp_cord = []
        for i in range(self.board_size):
            for j in range(self.board_size):
                if self.board[i][j] == self.me:
                    d += weights[i][j]
                    my_tiles += 1
                    my_cord.append((i, j))
                elif self.board[i][j] == self.opp:
                    d -= weights[i][j]
                    opp_tiles += 1
                    opp_cord.append((i, j))

        if my_tiles > opp_tiles:
            p = (100.0 * my_tiles) / (my_tiles + opp_tiles)
        elif my_tiles < opp_tiles:
            p = -(100.0 * opp_tiles) / (my_tiles + opp_tiles)
        else:
            p = 0

        c = self.cornersCalculate()
        l = self.nextToCorners()
        m = self.mobility()

        ranking = 0
        diags = [self.board[::-1, :].diagonal(i) for i in range(-3, 4)]
        diags.extend(self.board.diagonal(i) for i in range(3, -4, -1))
        diags = [n.tolist() for n in diags]
        for i in range(4):
            z = 0
            flag = False
            if flag == False:
                for o in diags[i * 4:(i + 1) * 4 + 1]:
                    z += 1
                    for a in o:
                        if a == self.me:
                            ranking += 3 * z

                        else:
                            flag = True
                            break
        for i in range(4):
            z = 0
            flag = False
            if flag == False:
                for o in diags[i * 4:(i + 1) * 4 + 1]:
                    z += 1
                    for a in o:
                        if a == self.opp:
                            ranking -= 3 * z

                        else:
                            flag = True
                            break

        if self.is_end():
            return 2 * p * 1000000
        return 2 * amount * p + ((9000 * c) + (382.026 * l) + (783.922 * m) + (10 * d) + 10 * ranking)

    def trim(self, moves, flag):
        best = []

        for i in moves:
            new_board = deepcopy(self)
            new_board.make_move(i, False)
            score = new_board.heuristic(0)
            pair = (score, new_board, i)
            best.append(pair)
        if flag:
            best.sort(key=lambda x: x[0])
        else:
            best.sort(reverse=True, key=lambda x: x[0])
        return best

    def find_best(self, depth, player):

        def alphabeta(state, depth, alpha, beta, maximizing_player, ile):

            if depth == 0 or state.is_end() or state.valid_moves(False) == [None]:
                return state.heuristic(ile)

            children = state.valid_moves(True)
            if maximizing_player:
                value = -math.inf
                for move in children:
                    new_board = deepcopy(state)
                    new_board.make_move(move, maximizing_player)
                    value = max(value, alphabeta(new_board, depth - 1, alpha, beta, False,  ile + 1))
                    alpha = max(alpha, value)
                    if beta <= alpha:
                        break

                return value
            else:
                value = math.inf
                children = state.valid_moves(True)
                for move in children:
                    new_board = deepcopy(state)
                    new_board.make_move(move, not maximizing_player)
                    value = min(value, alphabeta(new_board, depth - 1, alpha, beta, True, ile + 1))
                    beta = min(beta, value)
                    if beta <= alpha:
                        break

                return value

        best_move = None
        best_score = -math.inf
        if(player):
            best_score = math.inf
        mozliwe = self.trim(self.valid_moves(0), player)
        for board in mozliwe:
            val = alphabeta(board[1], depth, -math.inf, math.inf, player, 0)
            if(player):
                if val < best_score:
                    best_move = board[2]
                    best_score = val
            else:
                if val > best_score:
                    best_move = board[2]
                    best_score = val

        return best_move

def play_game():
    game_started = False
    gracz = True
    gra = Game(1)
    sys.stdout.write("RDY\n")
    sys.stdout.flush()
    while True:
        command = sys.stdin.readline().split()
        if command[0] == "ONEMORE":
            os.execl(sys.executable, sys.executable, *sys.argv)
        if command[0] == "BYE":
            exit(0)
        if not game_started:
            game_started = True
            if command[0] == "UGO":
                gracz = False
                gra = Game(0)
            # HEDID
            else:
                i, j = int(command[3]), int(command[4])
                gra.make_move((i, j), not gracz)
            moj_ruch = gra.find_best(3, gracz)
            gra.make_move(moj_ruch, gracz)
            sys.stdout.write("IDO ")
            sys.stdout.write(str(moj_ruch[0]))
            sys.stdout.write(" ")
            sys.stdout.write(str(moj_ruch[1]))
            sys.stdout.write("\n")
            sys.stdout.flush()
        else:
            i, j = int(command[3]), int(command[4])
            gra.make_move((i, j), not gracz)
            moj_ruch = gra.find_best(3, gracz)
            gra.make_move(moj_ruch, gracz)
            sys.stdout.write("IDO ")
            sys.stdout.write(str(moj_ruch[0]))
            sys.stdout.write(" ")
            sys.stdout.write(str(moj_ruch[1]))
            sys.stdout.write("\n")
            sys.stdout.flush()


play_game()








