import chess
import random
import math
from copy import deepcopy
import chess.pgn
import pandas as pd
from trie import PrefixTree

piece_values = {
    chess.PAWN: 1,
    chess.KNIGHT: 3,
    chess.BISHOP: 3,
    chess.ROOK: 5,
    chess.QUEEN: 9,
    chess.KING: 0

}

king_mid = [0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, -5, -5, -5, 0, 0,
            0, 0, 10, -5, -5, -5, 10, 0]

queen_mid = [-20, -10, -10, -5, -5, -10, -10, -20,
             -10, 0, 0, 0, 0, 0, 0, -10,
             -10, 0, 5, 5, 5, 5, 0, -10,
             -5, 0, 5, 5, 5, 5, 0, -5,
             -5, 0, 5, 5, 5, 5, 0, -5,
             -10, 5, 5, 5, 5, 5, 0, -10,
             -10, 0, 5, 0, 0, 0, 0, -10,
             -20, -10, -10, 0, 0, -10, -10, -20]

rook_mid = [10, 10, 10, 10, 10, 10, 10, 10,
            10, 10, 10, 10, 10, 10, 10, 10,
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 10, 10, 0, 0, 0,
            0, 0, 0, 10, 10, 5, 0, 0]

bishop_mid = [0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0,
              0, 10, 0, 0, 0, 0, 10, 0,
              5, 0, 10, 0, 0, 10, 0, 5,
              0, 10, 0, 10, 10, 0, 10, 0,
              0, 10, 0, 10, 10, 0, 10, 0,
              0, 0, -10, 0, 0, -10, 0, 0]

knight_mid = [-5, -5, -5, -5, -5, -5, -5, -5,
              -5, 0, 0, 10, 10, 0, 0, -5,
              -5, 5, 10, 10, 10, 10, 5, -5,
              -5, 5, 10, 15, 15, 10, 5, -5,
              -5, 5, 10, 15, 15, 10, 5, -5,
              -5, 5, 10, 10, 10, 10, 5, -5,
              -5, 0, 0, 5, 5, 0, 0, -5,
              -5, -10, -5, -5, -5, -5, -10, -5]

pawn_mid = [0, 0, 0, 0, 0, 0, 0, 0,
            30, 30, 30, 40, 40, 30, 30, 30,
            20, 20, 20, 30, 30, 30, 20, 20,
            10, 10, 15, 25, 25, 15, 10, 10,
            5, 5, 5, 20, 20, 5, 5, 5,
            5, 0, 0, 5, 5, 0, 0, 5,
            5, 5, 5, -10, -10, 5, 5, 5,
            0, 0, 0, 0, 0, 0, 0, 0]

evaluation = {
    'p': pawn_mid,
    'r': rook_mid,
    'b': bishop_mid,
    'n': knight_mid,
    'k': king_mid,
    'q': queen_mid
}


def heuristic(board, ile):
    score = 0
    if board.result() == '1-0':
        return math.inf
    numfigb = 0
    numfigw = 0
    white_pawns_left = len(board.pieces(chess.PAWN, chess.WHITE))
    black_pawns_left = len(board.pieces(chess.PAWN, chess.BLACK))
    for piece_type, value in piece_values.items():  #przewaga materialna
        mnoznik_bialy = 1
        mnoznik_czarny = 1
        if piece_type == chess.ROOK:  #jesli jest malo pionkow to wieze sa o wiele mocniejsze
            mnoznik_bialy = (8 - black_pawns_left) * 0.2
            mnoznik_czarny = (8 - white_pawns_left) * 0.2
        elif piece_type == chess.BISHOP:  #im mniej pionkow tym gonce maja wieksze potencjalne pole manewrowe, wiec tez dajemy lepsza pozycje
            mnoznik_bialy = (8 - black_pawns_left) * 0.05
            mnoznik_czarny = (8 - white_pawns_left) * 0.05

        score += value * len(board.pieces(piece_type, chess.WHITE)) * mnoznik_bialy
        score -= value * len(board.pieces(piece_type, chess.BLACK)) * mnoznik_czarny
        numfigb += len(board.pieces(piece_type, chess.BLACK))
        numfigw += len(board.pieces(piece_type, chess.WHITE))
    score2 = 0
    for square, piece in board.piece_map().items():  #gdzie jest na mapie - nagradzamy dobre pola, karzemy zle
        piece_type = piece.symbol().lower()
        if piece.color == chess.WHITE:
            score2 += evaluation[piece_type][square]
        else:
            score2 -= evaluation[piece_type][square]

    sum_distance = 0
    if numfigb <= 3 and numfigw >= 5:  #odleglosc czarnego krola do bialych figur w przypadku gdy figur czarnego jest malo, a bialego jest wzglednie duzo

        black_king = board.pieces(chess.KING, chess.BLACK)
        black_king = black_king.pop()

        white_pieces = board.pieces(chess.PAWN, chess.WHITE) | board.pieces(chess.KNIGHT, chess.WHITE) | \
                       board.pieces(chess.BISHOP, chess.WHITE) | board.pieces(chess.ROOK, chess.WHITE) | \
                       board.pieces(chess.QUEEN, chess.WHITE) | board.pieces(chess.KING, chess.WHITE)
        for i in white_pieces:
            sum_distance = chess.square_distance(i, black_king)

    #liczymy ile jest pionkow w tej samej linii i odejmujemy 1/2 za kazdego
    white_pawns = board.pieces(chess.PAWN, chess.WHITE)
    black_pawns = board.pieces(chess.PAWN, chess.BLACK)

    def count_pawns_by_file(pawns):
        file_counts = [0] * 8
        for pawn in pawns:
            file = chess.square_file(pawn)
            file_counts[file] += 1
        return sum((count - 1) * 0.5 for count in file_counts if count > 1)

    white_penalty = count_pawns_by_file(white_pawns)
    black_penalty = count_pawns_by_file(black_pawns)
    score += white_penalty - black_penalty

    return score + score2 / (ile / 8) - sum_distance * 20 + board.is_check() * 1000


def trim(self, moves, flag, ile):
    best = []

    for i in moves:
        new_board = deepcopy(self)
        new_board.push(i)
        score = heuristic(new_board, ile)
        pair = (score, new_board, i)
        best.append(pair)

    if flag:
        best.sort(key=lambda x: x[0])
    else:
        best.sort(reverse=True, key=lambda x: x[0])
    return best


def find_best(self, depth, player, ile):
    def alphabeta(state, depth, alpha, beta, player, maximizing_player, ile):
        if depth == 0 or state.is_game_over():
            return heuristic(state, ile)

        children = state.legal_moves
        if player == maximizing_player:
            value = -math.inf

            for move in children:
                # new_board = deepcopy(state)
                state.push(move)
                value = max(value, alphabeta(state, depth - 1, alpha, beta, not player, maximizing_player, ile + 1))
                alpha = max(alpha, value)
                state.pop()

                if alpha >= beta:
                    break
            return value
        else:
            value = math.inf

            for move in children:
                # new_board = deepcopy(state)
                state.push(move)
                value = min(value, alphabeta(state, depth - 1, alpha, beta, not player, maximizing_player, ile + 1))
                beta = min(beta, value)
                state.pop()
                if alpha >= beta:
                    break

            return value

    best_move = None
    best_score = -math.inf
    alpha = -math.inf
    beta = math.inf
    for board in trim(self, self.legal_moves, self.turn, ile):
        val = alphabeta(board[1], depth - 1, alpha, beta, board[1].turn, player, ile + 1)
        if val >= best_score:
            best_move = board[2]
            best_score = val
    return best_move

# openings = PrefixTree()
#
# def parse_book_opening():
#     f = pd.read_csv("openings_sheet.csv")
#     for i in range(len(f)):
#         ruchy = f.moves[i]
#         openings.insert(ruchy)
#
#         # Szukany prefiks jako string
#     # prefix = "a4 b6"
#     # print(openings.starts_with(prefix))
#
# parse_book_opening()
#
# def parse_moves(move_list):
#     moves = ""
#     for move in move_list:
#         napis = move.uci()
#         start = 0
#         for i in range(len(napis)):
#             if(napis[i-1] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']):
#                 start = i
#                 break
#         moves += napis[start:] + " "
#     return moves[:len(moves)-1]

num = 50
wins = 0
for i in range(1, num + 1):
    board = chess.Board()
    ile = 1
    # open_book = False
    while not board.is_game_over() and ile < 140:

        if board.turn == chess.WHITE:
            # if(open_book):
            #     last_moves = parse_moves(board.move_stack)
            #     kontynuacje = openings.starts_with(last_moves)
            #     if len(kontynuacje) == 0:
            #         open_book = False
            #     else:
            #         wybor = random.choice(kontynuacje)
            #         ruch = wybor.split(" ")[ile-1]
            #         board.push(ruch)
            # if not open_book:
                moves = find_best(board, 3, board.turn, ile)
                # print(moves)
                board.push(moves)
        else:
            moves = list(board.legal_moves)
            m = random.choice(moves)
            board.push(m)
        ile += 1
    else:
        print(board.result())

    if board.result() == '1-0':
        wins += 1
    print(i, wins, ile)
