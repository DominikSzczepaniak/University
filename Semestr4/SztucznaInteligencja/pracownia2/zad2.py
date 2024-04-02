from collections import deque
import itertools

#pomysl
#1 robimy permutacje ruchow i dla kazdej permutacji mnozymy kazdy ruch przez wielkosc mapy i pozniej na tym bfs i moze znajdzie wynik xd

class Commando:
    def __init__(self):
        self.map = []
        self.data_input()
        self.n = len(self.map)
        self.start_positions = set()
        self.walls = set()
        self.end_positions = set()
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if self.map[i][j] == "S":
                    self.start_positions.add((i, j))
                if self.map[i][j] == "B":
                    self.end_positions.add((i, j))
                    self.start_positions.add((i, j))
                if self.map[i][j] == "#":
                    self.walls.add((i, j))
                if self.map[i][j] == "G":
                    self.end_positions.add((i, j))
        self.horizontal = [1, -1, 0, 0]
        self.vertical = [0, 0, 1, -1]


    def data_input(self):
        with open("zad_input.txt", "r") as file:
            for line in file:
                self.map.append(list(line.strip()))
                self.m = len(self.map[0])

    def make_move(self, positions, dir):
        new_positions = set()

        for pos in positions:
            new_x = pos[0] + self.horizontal[dir]
            new_y = pos[1] + self.vertical[dir]

            if (new_x, new_y) not in self.walls:
                new_positions.add((new_x, new_y))
            else:
                new_positions.add((pos[0], pos[1]))
        return new_positions

    def end(self, positions):
        for position in positions:
            if position not in self.end_positions:
                return False
            
        return True
    
    def answer(self, moves):
        res = ""
        for move in moves:
            if move == 0:
                res += "D"
            elif move == 1:
                res += "U"
            elif move == 2:
                res += "R"
            elif move == 3:
                res += "L"
        f = open("zad_output.txt", "w")
        f.write(res)
    
    def oblicz(self, positions, moves):
        visited = set()
        queue = deque()
        queue.append((positions, moves))
        visited.add(str(positions))
        min_len = len(positions)

        while True:
            current_positions = queue.popleft()
            position, moves = current_positions[0], current_positions[1]
            if(self.end(position)):
                self.answer(moves)
                return
        
            for i in range(4):
                new_positions = self.make_move(position, i)
                if str(new_positions) not in visited:
                    if(len(new_positions) < min_len):
                        visited = set()
                        queue.clear()
                        min_len = len(new_positions)
                    visited.add(str(new_positions))
                    queue.append((new_positions, moves + [i]))

    def solve(self):
        moves_list = ['0', '1', '2', '3']
        all_moves = list(itertools.permutations(moves_list))
        min_moves = 10000000000
        best_moves = []
        best_positions = []

        for i in range(len(all_moves)):
            sequence = all_moves[i]
            current_positions = self.start_positions.copy()
            current_sequence = []
            current_moves = []

            for seq in sequence:
                current_sequence += seq * self.n

            for move in current_sequence:
                current_positions = self.make_move(current_positions, int(move))
                current_moves.append(int(move))

            if len(current_positions) < min_moves:
                min_moves = len(current_positions)
                best_moves = current_moves
                best_positions = current_positions
        self.oblicz(best_positions, best_moves) #zaczynamy tam gdzie usuwanie niepewnosci jest najlepsze potencjalnie




if __name__=="__main__":
    komandos = Commando()
    komandos.solve()
        