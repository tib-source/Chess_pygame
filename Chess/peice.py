import pygame
from .constants import SQUARE
import os
class Piece():
    def __init__(self, col:int, row:int, color:str) -> None:
        self.killed = False
        self.color = color
        self.row = row
        self.col = col
        self.image = None
        self.name:str
        self.x:int
        self.y:int
        self.getPos()

    def setWhite(self):
        self.white = True

    def isKilled(self):
        self.killed = True
        
    def getPos(self):
        self.x = self.col*SQUARE 
        self.y = self.row*SQUARE 

    def draw(self, color, screen):
        if self.image == None:
            self.image = pygame.image.load(f"asset\\{self.name.upper()}_{color.upper()}.png").convert_alpha()
        screen.blit(self.image, pygame.Rect(self.x, self.y, 10 ,10 ))
        pygame.display.update()

class King(Piece):
    def __init__(self,row,col,color) -> None:
        super(King, self).__init__(row,col,color)
        self.isCastled = False
        self.name = "King"
    
    def canMove(self, start:object, end:object) -> bool:
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
        super(Queen, self).__init__(row,col,color)
        self.name = "Queen"
    def canMove(self, board:object, start:object, end:object) -> bool:
        pass


class Knight(Piece):
    def __init__(self,row,col,color) -> None:
        super(Knight, self).__init__(row,col,color)
        self.name = "Knight"

    def canMove(self, board:object, start:object, end:object):
        pass



class Bishop(Piece):
    def __init__(self,row,col,color) -> None:
        super(Bishop, self).__init__(row,col,color)
        self.name = "Bishop"

    def canMove(self, board:object, start:object, end:object):
        pass

  

class Rook(Piece):
    def __init__(self,row,col,color) -> None:
        super(Rook, self).__init__(row,col,color)
        self.name = "Rook"

    def canMove(self, board:object, start:object, end:object):
        pass


class Pawn(Piece):
    def __init__(self, row,col, color) -> None:
        super(Pawn, self).__init__(row,col,color)
        self.name = "Pawn"
        self.firstMove = True
    
    def first(self):
        self.firstMove = False
        pass

    def canMove(self, board:object, start:object, end:object):
        y  = end.y - start.x
        if self.firstMove == True:
            if end.Piece:
                return False
            elif y <= 2 :
                self.firstMove = False
                return True
        else:
            return True if y == 1 else False

