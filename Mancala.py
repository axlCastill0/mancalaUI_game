
class Mancala() :
    def __init__(self, grid) :
        self.grid = grid
        self.difficulty = 0
        self.currentTurn = 0
        self.opposite_pit_mapping = {0 : 12, 1 : 11, 2 : 10, 3 : 9, 4 : 8, 5 : 7, 7 : 5, 8 : 4, 9 : 3, 10 : 2, 11 : 1, 12 : 0}

    def newGrid(self) :
        self.grid = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]

    def playerMove(self, id) :
        return True
    
    def cpuMove(self) :
        return True
    
    def checkWinner(self) :
        return True