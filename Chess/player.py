class Player:
    def __init__(self) -> None:
        self.whiteSide = False
        self.moves = [] 
        self.listKilled = []
    def setWhite(self):
        self.whiteSide = True
        pass

    def addKill(self, piece:object) -> None:
        self.listKilled.append(piece)
        pass

    def addMove(self, piece, start, end) -> None:
        self.moves.append((piece, start, end))
        pass
    
    def recentMove(self):
        return self.moves[-1]