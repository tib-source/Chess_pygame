from pygame import draw
from Chess.constants import BLACK


class Player:
    def __init__(self) -> None:
        self.turn = BLACK
        self.selected = None
        self.moves = [] 
        self.listKilled = []
        self.valid_moves = []

    def update(self)
        self.board. 
    def addKill(self, piece:object) -> None:
        self.listKilled.append(piece)
        pass

    def addMove(self, piece, start, end) -> None:
        self.moves.append((piece, start, end))
        pass
    
    def recentMove(self):
        return self.moves[-1]