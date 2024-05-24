import numpy as np
import random
import math
import time
import copy

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
        for i in range(board_size):
            for j in range(board_size):
                if self.board[i][j] is None:
                    self.freeCells.add((i, j))

    def __str__(self):
        answer = ""
        for i in range(self.board_size):
            for j in range(self.board_size):
                if self.board[i][j] is None:
                    answer += "."
                elif self.board[i][j] == 0:
                    answer += "B"
                else:
                    answer += "W"
            answer += "\n"
        return answer

    def in_board(self, i, j):
        return 0 <= i < self.board_size and 0 <= j < self.board_size

    def can_place(self, i, j, color):
        if self.board[i][j] != None:
            return False
        for dx, dy in dirs:
            x, y = i + dx, j + dy
            if not self.in_board(x, y):
                continue
            if self.board[x][y] == 1 - color:
                x += dx
                y += dy
                while self.in_board(x, y):
                    if self.board[x][y] == None:
                        break
                    if self.board[x][y] == color:
                        return True
                    x += dx
                    y += dy
        return False

    def valid_moves(self, color):
        moves = []
        for cell in self.freeCells:
            i, j = cell
            if self.can_place(i, j, color):
                moves.append((i, j))
        if moves.__len__() == 0:
            moves.append(None)
        return moves

    def make_move(self, move, color):
        self.history.append(self.board)
        self.moves_list.append(move)
        if move == None:
            return
        i, j = move
        i0, j0 = move
        self.board[i][j] = color
        self.freeCells -= {move}
        for dx, dy in dirs:
            x, y = i0 + dx, j0 + dy
            to_flip = []
            if not self.in_board(x, y):
                continue
            while self.in_board(x, y) and self.board[x][y] == 1 - color:
                to_flip.append((x, y))
                x += dx
                y += dy
            if self.in_board(x, y) and self.board[x][y] == color:
                for (x, y) in to_flip:
                    self.board[x][y] = color

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
            if not flag:
                for o in diags[i * 4:(i + 1) * 4 + 1]:
                    z += 1
                    for a in o:
                        if a == self.opp:
                            ranking -= 3 * z
                        else:
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
                    value = max(value, alphabeta(new_board, depth - 1, alpha, beta, False, ile + 1))
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
        mozliwe = self.trim(self.valid_moves(0), player)

        for board in mozliwe:
            val = alphabeta(board[1], depth, -math.inf, math.inf, player, 0)
            if val > best_score:
                best_move = board[2]
                best_score = val

        return best_move


    def mcts(state, iterations, root):

        root = Node(state, True)
        if len(state.valid_moves(True)) == 1:
            return state.valid_moves(True)[0]
        elif len(state.valid_moves(True)) == 0:
            return None
        # print(state.moves(True))z
        start = time.time()

        for _ in range(iterations):
            if time.time() - start > 0.5:
                break
            selected_node = root.select()
            selected_node.expand()
            # print("chuj")
            if len(selected_node.children) > 0:
                simulation_node = selected_node.select()
            else:
                simulation_node = selected_node
            score = simulation_node.simulate(simulation_node.player)
            simulation_node.backpropagate(score)
        best_child = max(root.children, key=lambda child: child.visits)
        # print(state.moves(True))
        # print(best_child.movi)
        return best_child


class Node:
    def __init__(self, board, player):
        self.state = board
        self.parent = None
        self.movi = ()
        self.children = []
        self.visits = 0
        self.score = 0
        self.player = player

    def uct(node, C=math.sqrt(2)):

        if node.visits == 0:
            return float('inf')
        exploitation = node.score / node.visits
        if node.parent == None:
            vis = 1
        else:
            vis = node.parent.visits
        exploration = math.sqrt(math.log(vis) / node.visits)
        return exploitation + C * exploration

    def select(node):
        while node.children:
            maxx = -math.inf
            for nodee in node.children:
                if nodee.uct() > maxx:
                    node = nodee
                    maxx = nodee.uct()
        return node

    def expand(node):
        legal_moves = node.state.valid_moves(True)
        for move in legal_moves:
            board = copy.deepcopy(node.state)

            board.make_move(move, True)
            new_node = Node(board, True)

            new_node.parent = node
            new_node.movi = move
            new_node.player = 1 - node.player

            node.children.append(new_node)

    def simulate(node, current_player):

        temp_state = copy.deepcopy(node.state)
        while not temp_state.is_end():
            legal_moves = temp_state.valid_moves(current_player)
            move = random.choice(legal_moves)
            temp_state.make_move(move, current_player)
            current_player = 1 - current_player
        if temp_state.score() > 0:
            winner = 0
        else:
            winner = 1
        if winner == True:
            return 1
        else:
            return 0

    def backpropagate(node, score):
        while node:
            node.visits += 1
            node.score += score
            node = node.parent


me = 0
nr = 10
sumGames = 0


for z in range(1, nr+1):
    game = Game(me)
    i = 0
    player = 0
    Flag = True
    root = Node(game, True)
    while True and Flag:
        if game.is_end():
            break
        if not player:
            # start = time.time()
            if game.valid_moves(True) == 0:
                continue

            node = game.mcts(50000, root)
            if isinstance(node, Node):
                root = node
                game.make_move(node.movi, True)
            else:
                game.make_move(node, True)
            # print("MCTS", time.time()-start)
        else:
            # start = time.time()
            if game.valid_moves(False) == 0:
                continue
            best = game.find_best(4, False)

            game.make_move(best, False)
            # print("ALPHABETA", time.time()-start)
        player = 1 - player

        i += 1

    if game.score() >= 0:
        sumGames += 1
    print('Game number: ', z, ", won till now: ", sumGames, ", lost till now: ", z - sumGames, " score in this game: ",
          game.score(),
          " rounds played: ", i)