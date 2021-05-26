import pygame
from Chess.spot import Spot
from Chess.constants import SQUARE

class Piece():
    def __init__(self, row, col, white:bool) -> None:
        self.killed = False
        self.white = white
        self.row = row
        self.col = col


        self.x:int
        self.y:int
        self.getPos()

    def setWhite(self):
        self.white = True

    def isKilled(self):
        self.killed = True
        
    def getPos(self):
        self.x = self.col*SQUARE - SQUARE//2
        self.y = self.row*SQUARE - SQUARE//2

    def draw(self, window, sprite):
        pygame.load()




class King(Piece):
    def __init__(self) -> None:
        self.killed = False
        self.white = False
        self.isCastled = False
    
    



    def canMove(self, start:Spot, end:Spot) -> bool:
        # TODO: write the conditions for a stalements and what not 
        if end.Piece.white == self.white:
            return False
        else: 
            y = abs(end.y - start.y)
            x = abs(end.x - start.x)
            if x == y == 1: 
                return True

    def isValidCastle(self, Board, start, end) -> bool:
        # TODO: write the logic for checking castling here
        pass


    def Castle(self, start, end) -> None:
        # TODO: write the logic for performing a castling here
        pass

    
class Queen(Piece):
    def __init__(self) -> None:
        self.killed = False
        self.white = False
    
    def setWhite(self):
        self.white = True
        pass

    def isKilled(self):
        self.killed = True
        pass

    def canMove(self, board:object, start:Spot, end:Spot) -> bool:
        pass

class Knight(Piece):
    def __init__(self) -> None:
        self.killed = False
        self.white = False
        pass

    def setWhite(self):
        self.white = True
        pass

    def isKilled(self):
        self.killed = True
        pass

    def canMove(self, board:object, start:Spot, end:Spot):
        pass

class Bishop(Piece):
    def __init__(self) -> None:
        self.killed = False
        self.white = False
    
    def setWhite(self):
        self.white = True
        pass

    def isKilled(self):
        self.killed = True
        pass

    def canMove(self, board:object, start:Spot, end:Spot):
        pass

class Rook(Piece):
    def __init__(self) -> None:
        self.killed = False
        self.white = False
    
    def setWhite(self):
        self.white = True
        pass

    def isKilled(self):
        self.killed = True
        pass

    def canMove(self, board:object, start:Spot, end:Spot):
        pass

class Pawn(Piece):
    def __init__(self) -> None:
        self.killed = False
        self.white = False
        self.firstMove = True

    
    def setWhite(self):
        self.white = True
        pass

    def isKilled(self):
        self.killed = True
        pass
    
    def first(self):
        self.firstMove = False
        pass

    def canMove(self, board:object, start:Spot, end:Spot):
        y  = end.y - start.x
        if self.firstMove == True:
            if end.Piece:
                return False
            elif y <= 2 :
                self.firstMove = False
                return True
        else:
            return True if y == 1 else False