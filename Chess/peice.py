import pygame
from .constants import BOARD_LENGTH, SQUARE, WHITE


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
        self.possible_moves = []

    def setWhite(self):
        self.white = True

    def isKilled(self):
        self.killed = True
        
    def getPos(self):
        self.x = self.col*SQUARE 
        self.y = self.row*SQUARE 

    def draw(self, color, screen):
        if self.image == None:
            color_ = "WHITE" if WHITE == color else "BLACk" 
            self.image = pygame.image.load(f"asset\\{self.name.upper()}_{color_.upper()}.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (80, 80))
        screen.blit(self.image, pygame.Rect(self.x+10, self.y+10, 100 ,10 ))
        pygame.display.update()

class King(Piece):
    def __init__(self,col,row,color) -> None:
        super(King, self).__init__(col,row,color)
        self.isCastled = False
        self.name = "King"
    
    def canMove(self, start:object, end:object, board:object) -> bool:
        # TODO: write the conditions for a stalements and what not 
        if end.Piece:
            if end.Piece.color.lower() == self.color.lower():
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
    def __init__(self,col,row,color) -> None:
        super(Queen, self).__init__(col,row,color)
        self.name = "Queen"
    def canMove(self, start:object, end:object, board:object) -> bool:
        pass


class Knight(Piece):
    def __init__(self,col,row,color) -> None:
        super(Knight, self).__init__(col,row,color)
        self.name = "Knight"

    def canMove(self, start:object, end:object, board:object):
        pass



class Bishop(Piece):
    def __init__(self,col,row,color) -> None:
        super(Bishop, self).__init__(col,row,color)
        self.name = "Bishop"

    def canMove(self, start:object, end:object, board:object):
        pass

  

class Rook(Piece):
    def __init__(self,col,row,color) -> None:
        super(Rook, self).__init__(col,row,color)
        self.name = "Rook"
        

    def canMove(self, start:object, end:object, board:object):
        self.possible_moves = []
        for i in board[start.Piece.row]:
            if i.Piece == 0 or i.Piece.color != self.color:
                self.possible_moves.append(i)
                continue
            elif i.Piece.color == self.color:
                break
        for i in range(BOARD_LENGTH):
            spot = board[i][start.col]
            if spot.Piece == 0 or spot.Piece.color != self.color: 
                self.possible_moves.append(board[i][start.Piece.col])
                continue
            elif spot.Piece.color == self.color:
                break
        if end in set(self.possible_moves):
            print(set(self.possible_moves))
            return True
        return False

class Pawn(Piece):
    def __init__(self, col,row, color) -> None:
        super(Pawn, self).__init__(col,row,color)
        self.name = "Pawn"
        self.firstMove = True
    
    def first(self):
        self.firstMove = False
        pass

    def canMove(self, start:object, end:object, board):
        y  = abs(end.row - start.row)
        x= end.col - start.col
        if x == 0:
            if self.firstMove == True:
                if end.Piece:
                    return False
                elif y <= 2 :
                    self.firstMove = False
                    return True
            else:
                return True if y == 1 else False
        else:
            print("INVALID MOVE")

