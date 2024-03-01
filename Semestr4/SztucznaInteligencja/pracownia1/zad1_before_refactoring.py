directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
rook_directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def convert_to_pair(coordinate):
    """Return pair (1-8, 1-8)"""
    return ord(coordinate[0]) - 96, int(coordinate[1])


def convert_to_position(pair):
    """Return position (a-h, 1-8)"""
    return chr(pair[0] + 96) + str(pair[1])


def check_input(white_king, black_king,
                white_rook):
    """Checks if input is possible - whether there are kings next to each other or any two pieces are on the same
    square"""
    if (white_king == black_king or white_king == white_rook or black_king == white_rook):
        return False
    white_king = convert_to_pair(white_king)
    black_king = convert_to_pair(black_king)
    for direction in directions:
        if white_king[0] + direction[0] == black_king[0] and white_king[1] + direction[1] == black_king[1]:
            return False
    return True


def inside_board(position):
    """Checks if position is inside the board"""
    return 0 < position[0] < 9 and 0 < position[1] < 9


def viable_move(white_king, white_rook, black_king, id):  # sprawdzamy czy ruch jest mozliwy
    if (id == 1):  # bialy krol
        if (not inside_board(white_king)):
            return False
        if white_king == white_rook or white_king == black_king:
            return False
        for kierunek in directions:
            new_position = (white_king[0] + kierunek[0], white_king[1] + kierunek[1])
            if (not inside_board(new_position)):
                continue
            if new_position == black_king:
                return False
        return True
    if (id == 2):  # biala wieza
        if (not inside_board(white_rook)):
            return False
        if (white_rook == white_king or white_rook == black_king):
            return False
        for kierunek in directions:
            new_position = (white_rook[0] + kierunek[0], white_rook[1] + kierunek[1])
            if (not inside_board(new_position)):
                continue
            if new_position == black_king:
                return False
        return True
    if (id == 3):  # czarny krol
        if (not inside_board(black_king)):
            return False
        if black_king[0] == white_rook[0] or black_king[1] == white_rook[1]:
            return False
        for kierunek in directions:
            new_position = (black_king[0] + kierunek[0], black_king[1] + kierunek[1])
            if (not inside_board(new_position)):
                continue
            if new_position == white_king:
                return False
        return True


def possible_move(white_king, white_rook, black_king):  # sprawdzamy czy jakikolwiek ruch czarnego krola jest mozliwy
    for kierunek in directions:
        new_position = (black_king[0] + kierunek[0], black_king[1] + kierunek[1])
        mozna = True
        if not inside_board(new_position):
            continue
        # sprawdzmy czy wieza jest w tym samym rzedzie lub kolumnie
        if new_position[0] == white_rook[0] or new_position[1] == white_rook[1]:
            mozna = False
        # sprawdzmy czy krol jest w zasiegu ruchu
        for kierunek2 in directions:
            if new_position[0] + kierunek2[0] == white_king[0] and new_position[1] + kierunek2[1] == white_king[1]:
                mozna = False
        if mozna:
            return True
    return False


def check_draw(color, white_king, white_rook, black_king):  # sprawdzamy czy jest pat
    if (not possible_move(white_king, white_rook, black_king) and (
            white_rook[0] != black_king[0] and white_rook[1] != black_king[1])):
        return True
    return False


def is_checkmate(white_king, white_rook, black_king):
    if (not possible_move(white_king, white_rook, black_king) and (
            white_rook[0] == black_king[0] or white_rook[1] == black_king[1])):
        return True
    return False


def debug_mode(start_color, white_king, white_rook, black_king):
    white_king = convert_to_pair(white_king)
    white_rook = convert_to_pair(white_rook)
    black_king = convert_to_pair(black_king)
    if check_draw(start_color, white_king, white_rook, black_king):
        return "INF"
    if (is_checkmate(white_king, white_rook, black_king)):
        return 0
    queue = []
    queue.append((white_king, white_rook, black_king, start_color, 0, []))
    visited = set()
    while queue:
        white_king, white_rook, black_king, color, moves, what_moves = queue.pop(0)
        if ((white_king, white_rook, black_king) in visited):
            continue
        visited.add((white_king, white_rook, black_king))
        if color == "white":
            for kierunek in directions:
                new_position1 = (white_king[0] + kierunek[0], white_king[1] + kierunek[1])
                if ((new_position1, white_rook, black_king) in visited):
                    continue
                if viable_move(new_position1, white_rook, black_king, 1):
                    if is_checkmate(new_position1, white_rook, black_king):
                        return moves + 1, what_moves + [
                            convert_to_position(white_king) + "" + convert_to_position(new_position1)]
                    queue.append((new_position1, white_rook, black_king, "black", moves + 1,
                                  what_moves + [convert_to_position(white_king) + convert_to_position(new_position1)]))
            for kierunek in rook_directions:
                for zasieg in range(1, 8):
                    new_position2 = (white_rook[0] + kierunek[0] * zasieg, white_rook[1] + kierunek[1] * zasieg)
                    if ((white_king, new_position2, black_king) in visited):
                        continue
                    if viable_move(white_king, new_position2, black_king, 2):
                        if is_checkmate(white_king, new_position2, black_king):
                            return moves + 1, what_moves + [
                                convert_to_position(white_rook) + convert_to_position(new_position2)]
                        queue.append((white_king, new_position2, black_king, "black", moves + 1, what_moves + [
                            convert_to_position(white_rook) + convert_to_position(new_position2)]))
        else:
            for kierunek in directions:
                new_position = (black_king[0] + kierunek[0], black_king[1] + kierunek[1])
                if ((white_king, white_rook, new_position) in visited):
                    continue
                if viable_move(white_king, white_rook, new_position, 3):
                    if is_checkmate(new_position, white_rook, new_position):
                        return moves + 1, what_moves + [
                            convert_to_position(black_king) + convert_to_position(new_position)]
                    queue.append((white_king, white_rook, new_position, "white", moves + 1,
                                  what_moves + [convert_to_position(black_king) + convert_to_position(new_position)]))


def evaluate_mode(start_color, white_king, white_rook, black_king):
    white_king = convert_to_pair(white_king)
    white_rook = convert_to_pair(white_rook)
    black_king = convert_to_pair(black_king)
    if check_draw(start_color, white_king, white_rook, black_king):
        return "INF"
    if (is_checkmate(white_king, white_rook, black_king)):
        return 0
    queue = []
    queue.append((white_king, white_rook, black_king, start_color, 0))
    visited = set()
    while queue:
        white_king, white_rook, black_king, color, moves = queue.pop(0)
        if ((white_king, white_rook, black_king) in visited):
            continue
        visited.add((white_king, white_rook, black_king))
        if color == "white":
            for kierunek in directions:
                new_position1 = (white_king[0] + kierunek[0], white_king[1] + kierunek[1])
                if viable_move(new_position1, white_rook, black_king, 1):
                    if is_checkmate(new_position1, white_rook, black_king):
                        return moves + 1
                    queue.append((new_position1, white_rook, black_king, "black", moves + 1))
            for kierunek in rook_directions:
                for zasieg in range(1, 8):
                    new_position2 = (white_rook[0] + kierunek[0] * zasieg, white_rook[1] + kierunek[1] * zasieg)
                    if viable_move(white_king, new_position2, black_king, 2):
                        if is_checkmate(white_king, new_position2, black_king):
                            return moves + 1
                        queue.append((white_king, new_position2, black_king, "black", moves + 1))
        else:
            for kierunek in directions:
                new_position = (black_king[0] + kierunek[0], black_king[1] + kierunek[1])
                if viable_move(white_king, white_rook, new_position, 3):
                    if is_checkmate(new_position, white_rook, new_position):
                        return moves + 1
                    queue.append((white_king, white_rook, new_position, "white", moves + 1))


if __name__ == "__main__":
    file = open("zad1_input.txt", "r")
    for line in file:
        start_color, white_king, white_rook, black_king = line.split()
        if not check_input(white_king, white_rook, black_king):
            print("INF")
            continue
        # wynik, ruchy = debug_mode(start_color, white_king, white_rook, black_king)
        wynik = evaluate_mode(start_color, white_king, white_rook, black_king)
        f = open("zad1_output.txt", "w")
        f.write(str(wynik))
