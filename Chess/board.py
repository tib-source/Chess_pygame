
from Chess.constants import *
from Chess.spot import Spot
class Board:
    def __init__(self) -> None:
        self.SQUARE = WIDTH//BOARD_LENGTH
        self.BOARD_LENGTHBOARD_LENGTH = 8
        self.gameBoard = [[(j*SQUARE,i*SQUARE) for j in range(1, BOARD_LENGTH+1)]for i in range(1, BOARD_LENGTH+1)]

    def drawBoard(self,screen):
        for x in range(self.BOARD_LENGTH):
            for y in range(x%2,self.BOARD_LENGTH,2):
                pygame.draw.rect(screen, WHITE, pygame.Rect(x*SQUARE,y*SQUARE,SQUARE,SQUARE))
    def resetBoard(self):
        #TODO: this assignement is fucked, I want it so that i can acces the Spot objects
        #TODO: find a way to store these Objects.
        #TODO: i need them for calculating moves and etc in the Game Class 
        #white 
        Spot( self.gameBoard[7][0] , self.gameBoard[0][1] , Rook.setWhite())
        Spot( self.gameBoard[7][0] , self.gameBoard[1][1] , Knight.setWhite())
        Spot( self.gameBoard[7][0] , self.gameBoard[2][1] , Bishop.setWhite())
        Spot( self.gameBoard[6][0] , self.gameBoard[0][1] , Pawn.setWhite())
        Spot( self.gameBoard[6][0] , self.gameBoard[1][1] , Pawn.setWhite())
        Spot( self.gameBoard[6][0] , self.gameBoard[2][1] , Pawn.setWhite())


        #black
        Spot( self.gameBoard[0][0] , self.gameBoard[0][1] , Rook)
        Spot( self.gameBoard[0][0] , self.gameBoard[1][1] , Knight)
        Spot( self.gameBoard[0][0] , self.gameBoard[2][1] , Bishop)
        Spot( self.gameBoard[1][0] , self.gameBoard[0][1] , Pawn)
        Spot( self.gameBoard[1][0] , self.gameBoard[1][1] , Pawn)
        Spot( self.gameBoard[1][0] , self.gameBoard[2][1] , Pawn)
        pass
        
        for i in range(2,6):
            for j in range(0, 8):
                Spot(self.gameBoard[j][0], self.gameBoard[i][1], None)