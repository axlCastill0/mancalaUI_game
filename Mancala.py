import random

class Mancala() :
    def __init__(self, grid) :
        self.grid = grid
        self.difficulty = 0
        self.currentTurn = 0
        self.firstTurn = 0
        self.gameEnded = 0
        self.opposite_pit_mapping = {0 : 12, 1 : 11, 2 : 10, 3 : 9, 4 : 8, 5 : 7, 7 : 5, 8 : 4, 9 : 3, 10 : 2, 11 : 1, 12 : 0}

    def newGrid(self) :
        self.grid = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]
        self.gameEnded = 0
        if self.firstTurn == 1 :
            self.currentTurn = 1
            if self.difficulty == 0:
                self.cpuMove()
            elif self.difficulty == 1:
                self.cpuMoveMax()
            elif self.difficulty == 2:
                self.cpuMoveMinMax()

    def playerMove(self, id) :
        i = self.grid[id]
        self.grid[id] = 0
    
        for x in range(i):
            if id + x + 1 == 13:
                x = x - 1
            elif id + x + 1 > 13:
                id = - x - 1
                self.grid[id + x + 1] += 1
            else:
                self.grid[id + x + 1] += 1

            if (x == i - 1) and (self.grid[id + x + 1] == 1) and ((id + x + 1) != 6) and ((id + x + 1) != 13) and (self.grid[self.opposite_pit_mapping[id + x + 1]] != 0):
                if (id + x + 1 != 7) and (id + x + 1 != 8) and (id + x + 1 != 9) and (id + x + 1 != 10) and (id + x + 1 != 11) and (id + x + 1 != 12):
                    self.grid[6] += 1
                    self.grid[6] += self.grid[self.opposite_pit_mapping[id + x + 1]]
                    self.grid[id + x + 1] = 0
                    self.grid[self.opposite_pit_mapping[id + x + 1]] = 0
                
            if (x == i - 1) and (id + x + 1 == 6):
                self.currentTurn = 0
            else:
                self.currentTurn = 1
    
    def cpuMove(self) :
        while self.currentTurn != 0:
            
            ranId = random.randint(7, 12)
            index = 0
            while self.grid[ranId] == 0:
                if index == 6:
                    break
                ranId = random.randint(7, 12)
                index += 1
            
            if index == 6:
                break

            i = self.grid[ranId]
            self.grid[ranId] = 0

            for x in range(i):
                if ranId + x + 1 > 13:
                    ranId = - x - 1
                    self.grid[ranId + x + 1] += 1
                else:
                    self.grid[ranId + x + 1] += 1

                if (x == i - 1) and (self.grid[ranId + x + 1] == 1) and ((ranId + x + 1) != 6) and ((ranId + x + 1) != 13) and (self.grid[self.opposite_pit_mapping[ranId + x + 1]] != 0):
                    if (ranId + x + 1 != 0) and (ranId + x + 1 != 1) and (ranId + x + 1 != 2) and (ranId + x + 1 != 3) and (ranId + x + 1 != 4) and (ranId + x + 1 != 5):
                        self.grid[13] += 1
                        self.grid[13] += self.grid[self.opposite_pit_mapping[ranId + x + 1]]
                        self.grid[ranId + x + 1] = 0
                        self.grid[self.opposite_pit_mapping[ranId + x + 1]] = 0

                if (x == i - 1) and (ranId + x + 1 == 13):
                    self.currentTurn = 1
                else:
                    self.currentTurn = 0

    def cpuMoveMax(self):
        while self.currentTurn != 0:
            max_pit = -1
            max_stones = -1

            for i in range(7, 13):
                if self.grid[i] > max_stones:
                    max_stones = self.grid[i]
                    max_pit = i
            
            if max_stones == 0:
                break

            i = self.grid[max_pit]
            self.grid[max_pit] = 0

            for x in range(i):
                if max_pit + x + 1 > 13:
                    max_pit = - x - 1
                    self.grid[max_pit + x + 1] += 1
                else:
                    self.grid[max_pit + x + 1] += 1

                if (x == i - 1) and (self.grid[max_pit + x + 1] == 1) and ((max_pit + x + 1) != 6) and ((max_pit + x + 1) != 13) and (self.grid[self.opposite_pit_mapping[max_pit + x + 1]] != 0):
                    if (max_pit + x + 1 != 0) and (max_pit + x + 1 != 1) and (max_pit + x + 1 != 2) and (max_pit + x + 1 != 3) and (max_pit + x + 1 != 4) and (max_pit + x + 1 != 5):
                        self.grid[13] += 1
                        self.grid[13] += self.grid[self.opposite_pit_mapping[max_pit + x + 1]]
                        self.grid[max_pit + x + 1] = 0
                        self.grid[self.opposite_pit_mapping[max_pit + x + 1]] = 0

                if (x == i - 1) and (max_pit + x + 1 == 13):
                    self.currentTurn = 1
                else:
                    self.currentTurn = 0

    def cpuMoveMinMax(self):
        while self.currentTurn != 0:
            _, best_move = self.minimax(self.grid, self.currentTurn, depth=3)
        
            best_move = min(max(best_move, 7), 12)

            print(best_move)
        
            self.grid = self.performMove(self.grid, best_move)
            self.currentTurn = 1 - self.currentTurn

    def minimax(self, state, maximizing_player, depth):
        if depth == 0 or self.isTerminal(state):
            return self.evaluate(state), None

        if maximizing_player:
            max_eval = float('-inf')
            best_move = None
            for move in range(7, 13):
                if state[move] > 0:
                    new_state = self.performMove(state[:], move)
                    eval, _ = self.minimax(new_state, False, depth - 1)
                    if eval > max_eval:
                        max_eval = eval
                        best_move = move
            return max_eval, best_move
        else:
            min_eval = float('inf')
            best_move = None
            for move in range(0, 6):
                if state[move] > 0:
                    new_state = self.performMove(state[:], move)
                    eval, _ = self.minimax(new_state, True, depth - 1)
                    if eval < min_eval:
                        min_eval = eval
                        best_move = move
            return min_eval, best_move

    def evaluate(self, state):
        return state[6] - state[13]

    def isTerminal(self, state):
        return sum(state[:6]) == 0 or sum(state[7:13]) == 0

    def performMove(self, state, move):
        stones = state[move]
        state[move] = 0
        current_pit = move

        while stones > 0:
            current_pit = (current_pit + 1) % 14
            if current_pit != 6:
                state[current_pit] += 1
                stones -= 1

        if current_pit != 13 and state[current_pit] == 1 and state[current_pit] != 0:
            opposite_pit = 12 - current_pit
            if state[opposite_pit] > 0:
                state[13] += state[current_pit] + state[opposite_pit]
                state[current_pit] = 0
                state[opposite_pit] = 0

        return state
    
    def checkEmpty(self):
        cpuSum = 0
        plrSum = 0
        for i in range(6) :
            plrSum += self.grid[i]
        for i in range(7, 13) :
            cpuSum += self.grid[i]
        if cpuSum == 0 :
            self.grid[6] += plrSum
            for i in range(6) :
                self.grid[i] = 0
            self.gameEnded = 1
            return
        elif plrSum == 0:
            self.grid[13] += cpuSum
            for i in range(7, 13) :
                self.grid[i] = 0
            self.gameEnded = 2
        if self.grid[6] == self.grid[13] and self.grid == 24:
            self.gameEnded = 3
        