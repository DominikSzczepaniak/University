from collections import deque
import numpy as np
import heapq

class Commando:
    def __init__(self):
        self.map = []
        self.data_input()
        self.n = len(self.map)
        self.m = len(self.map[0])
        self.start_positions = set()
        self.walls = set()
        self.end_positions = set()
        self.minDistance = np.full((self.n, len(self.map[0])), 10000)
        for i in range(self.n):
            for j in range(self.m):
                if self.map[i][j] == "S":
                    self.start_positions.add((i, j))
                if self.map[i][j] == "B":
                    self.end_positions.add((i, j))
                    self.start_positions.add((i, j))
                if self.map[i][j] == "#":
                    self.walls.add((i, j))
                if self.map[i][j] == "G":
                    self.end_positions.add((i, j))
        self.vertical = [1, -1, 0, 0]
        self.horizontal = [0, 0, 1, -1]
        self.moveDirection = ["D", "U", "R", "L"]

        self.stopien = 2 #jak damy 20 to przechodzi wszystkie testy do zadania 2

    def data_input(self):
        with open("zad_input.txt", "r") as file:
            for line in file:
                self.map.append(list(line.strip()))

    def end(self, positions):
        for position in positions:
            if position not in self.end_positions:
                return False
        return True
    
    def answer(self, moves):
        f = open("zad_output.txt", "w")
        print(moves)
        f.write(moves)

    def runAllBFS(self):
        for pos in self.end_positions:
            self.minDistance[pos[0]][pos[1]] = 0
            self.BFS(pos)


    def BFS(self, position):
        visited = set()
        queue = deque()
        queue.append((position, 0))
        visited.add(position)
        while queue:
            current_position, moves = queue.popleft()
            self.minDistance[current_position[0]][current_position[1]] = min(self.minDistance[current_position[0]][current_position[1]], moves)
            for i in range(4):
                new_x = current_position[0] + self.vertical[i]
                new_y = current_position[1] + self.horizontal[i]
                if (new_x, new_y) not in visited and (new_x, new_y) not in self.walls:
                    queue.append(((new_x, new_y), moves + 1))
                    visited.add((new_x, new_y))


    def heuristic(self, positions):
        res = -1
        for pos in positions:
            res = max(res, self.minDistance[pos[0]][pos[1]])
        return res * self.stopien
    
    def check_moves(self, state):
        positions = state[0]
        moves = state[1]
        all_positions = []
        for i in range(4):
            new_positions = set()
            for pos in positions:
                new_x = pos[0] + self.vertical[i]
                new_y = pos[1] + self.horizontal[i]
                if (new_x, new_y) not in self.walls:
                    new_positions.add((new_x, new_y))
                else:
                    new_positions.add((pos[0], pos[1]))
            
            if(frozenset(new_positions) in self.visited and self.visitedWeight[frozenset(new_positions)] < len(moves) + 1):
                continue

            self.visited.add(frozenset(new_positions))
            self.visitedWeight[frozenset(new_positions)] = len(moves)
            
            all_positions.append((new_positions, moves + self.moveDirection[i]))
        return all_positions

    def AStar(self, positions, moves):
        Q = []
        heapq.heappush(Q, (self.heuristic(positions) + len(moves), (positions, moves)))
        self.visited = set()
        self.visited.add(frozenset(positions))
        self.visitedWeight = dict() 
        self.visitedWeight[frozenset(positions)] = 0

        while len(Q) > 0:
            state = heapq.heappop(Q)[1]

            new_states = self.check_moves(state)

            for new_state in new_states:
                if self.end(new_state[0]):
                    self.answer(new_state[1])
                    # self.Verbose(new_state[1])
                    return
                heapq.heappush(Q, (self.heuristic(new_state[0]) + len(new_state[1]), new_state))

    def Verbose(self, moves):
        positions = set()
        for pos in self.start_positions:
            positions.add(pos)
        for i in range(len(moves)):
            new_positions = set()
            ruch = moves[i]
            if ruch == 'D':
                for pos in positions:
                    new_x = pos[0] + 1
                    new_y = pos[1]
                    if (new_x, new_y) not in self.walls:
                        new_positions.add((new_x, new_y))
                    else:
                        new_positions.add((pos[0], pos[1]))
            elif ruch == 'U':
                for pos in positions:
                    new_x = pos[0] - 1
                    new_y = pos[1]
                    if (new_x, new_y) not in self.walls:
                        new_positions.add((new_x, new_y))
                    else:
                        new_positions.add((pos[0], pos[1]))
            elif ruch == 'R':
                for pos in positions:
                    new_x = pos[0] 
                    new_y = pos[1] + 1
                    if (new_x, new_y) not in self.walls:
                        new_positions.add((new_x, new_y))
                    else:
                        new_positions.add((pos[0], pos[1]))
            elif ruch == 'L':
                for pos in positions:
                    new_x = pos[0] 
                    new_y = pos[1] - 1
                    if (new_x, new_y) not in self.walls:
                        new_positions.add((new_x, new_y))
                    else:
                        new_positions.add((pos[0], pos[1]))
            self.printMap(new_positions)
            positions = new_positions
    
    def printMap(self, positions):
        for i in range(self.n):
            for j in range(self.m):
                if (i, j) in positions:
                    print("S", end = "")
                elif (i, j) in self.walls:
                    print("#", end = "")
                elif (i, j) in self.end_positions:
                    print("G", end = "")
                else:
                    print(" ", end = "")
            print()


if __name__=="__main__":
    komandos = Commando()   
    komandos.runAllBFS()
    komandos.AStar(komandos.start_positions, "")       
