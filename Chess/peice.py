import pygame
from .spot import Spot
from .constants import SQUARE, ASSETS_DIR
import os
class Piece():
    def __init__(self, row:int, col:int, color:str) -> None:
        self.killed = False
        self.color = color
        self.row = row
        self.col = col
        self.image = None
        self.name:str
        self.x:int
        self.y:int
        self.getPos()
        self.draw()

    def setWhite(self):
        self.white = True

    def isKilled(self):
        self.killed = True
        
    def getPos(self):
        self.x = self.col*SQUARE - SQUARE//2
        self.y = self.row*SQUARE - SQUARE//2

    def draw(self, window, color):
        if self.image == None:
            self.image = pygame.image.load(os.path.join(ASSETS_DIR,f"{self.name.upper()}_{color.upper()}.png"))
        self.rect = self.image.get_rect(self.x,self.y)

class King(Piece):
    def __init__(self,rol,col,color) -> None:
        super.__init__(rol,col,color)
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
    def __init__(self,row,col,color) -> None:
        super.__init__(row,col,color)
        self.name = "Queen"
    def canMove(self, board:object, start:Spot, end:Spot) -> bool:
        pass


class Knight(Piece):
    def __init__(self,row,col,color) -> None:
        super.__init__(row,col,color)
        self.name = "Knight"

    def canMove(self, board:object, start:Spot, end:Spot):
        pass



class Bishop(Piece):
    def __init__(self,row,col,color) -> None:
        super.__init__(row,col,color)
        self.name = "Bishop"

    def canMove(self, board:object, start:Spot, end:Spot):
        pass

  

class Rook(Piece):
    def __init__(self,row,col,color) -> None:
        super.__init__(row,col,color)
        self.name = "Rook"

    def canMove(self, board:object, start:Spot, end:Spot):
        pass


class Pawn(Piece):
    def __init__(self, row,col, color) -> None:
        super.__init__(row,col,color)
        self.name = "Pawn"
        self.firstMove = True
    
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

