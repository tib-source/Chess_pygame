import pygame
from .peice import *
from .spot import Spot
from .constants import (
    WIDTH,
    BOARD_LENGTH,
    WHITE,
)


class Board:
    def __init__(self) -> None:
        self.SQUARE = WIDTH//BOARD_LENGTH
        self.board = [[] for _ in range(8)]
        self.gameBoard = [[(col, row) for col in range(0, BOARD_LENGTH)]for row in range(0, BOARD_LENGTH)]
        

    def drawBoard(self,screen):
        for x in range(BOARD_LENGTH):
            for y in range(x%2,BOARD_LENGTH,2):
                pygame.draw.rect(screen, WHITE, pygame.Rect(x*SQUARE,y*SQUARE,SQUARE,SQUARE))

    def create_board(self,screen):
        #WHITE 
        Rook_0_White =   Rook( self.gameBoard[0][0][0] , self.gameBoard[0][0][1] , "White" )        
        Bishop_0_White = Bishop( self.gameBoard[0][1][0] , self.gameBoard[0][1][1] , "White" )        
        Knight_0_White = Knight( self.gameBoard[0][2][0] , self.gameBoard[0][2][1] , "White" )        
        King_0_White =   King( self.gameBoard[0][3][0] , self.gameBoard[0][3][1] , "White" )        
        Queen_0_White =  Queen( self.gameBoard[0][4][0] , self.gameBoard[0][4][1] , "White" )        
        Knight_1_White = Knight( self.gameBoard[0][5][0] , self.gameBoard[0][5][1] , "White" )        
        Bishop_1_White = Bishop( self.gameBoard[0][6][0] , self.gameBoard[0][6][1] , "White" )        
        Rook_1_White =   Rook( self.gameBoard[0][7][0] , self.gameBoard[0][7][1] , "White" )

        wh_list = [
            Rook_0_White,
            Bishop_0_White,
            Knight_0_White,
            King_0_White,
            Queen_0_White,
            Knight_1_White,
            Bishop_1_White,
            Rook_1_White
        ]

        for i, x in enumerate(wh_list):
            x.draw(x.color, screen)
            self.board[0].append( Spot( 0*SQUARE, i*SQUARE, x ))
        Pawns = {}
        for i in range(0, BOARD_LENGTH):
            Pawns["p "+str(i)+" w"] = Pawn_ = Pawn( self.gameBoard[1][i][0], self.gameBoard[1][i][1], "White")
            Pawn_.draw(Pawn_.color, screen)
            self.board[1].append( Spot( 1*SQUARE, i*SQUARE, Pawn_ ))
        
        # for i in range(0, BOARD_LENGTH):
        #     Pawn( self.gameBoard[1][i][0], self.gameBoard[1][i][1], "White")


        #Pawn_0_White = Rook(self.gameBoard[0][0][0], self.gameBoard[0][1][0],"White")

        #BLACK
        # Rook_0_Black =      self.board[7].append ( Spot( 7*SQUARE, 0*SQUARE, (Rook( self.gameBoard[7][0][0] , self.gameBoard[7][0][1] , "White" ) ) ) )
        # Bishop_0_Black =    self.board[7].append ( Spot( 7*SQUARE, 1*SQUARE, (Bishop( self.gameBoard[7][1][0] , self.gameBoard[7][1][1] , "Black" ) ) ) )
        # Knight_0_Black =    self.board[7].append ( Spot( 7*SQUARE, 2*SQUARE, (Knight( self.gameBoard[7][2][0] , self.gameBoard[7][2][1] , "Black" ) ) ) )
        # King_0_Black =      self.board[7].append ( Spot( 7*SQUARE, 3*SQUARE, (King( self.gameBoard[7][3][0] , self.gameBoard[7][3][1] , "Black" ) ) ) )
        # Queen_0_Black =     self.board[7].append ( Spot( 7*SQUARE, 4*SQUARE, (Queen( self.gameBoard[7][4][0] , self.gameBoard[7][4][1] , "Black" ) ) ) )
        # Knight_1_Black =    self.board[7].append ( Spot( 7*SQUARE, 5*SQUARE, (Knight( self.gameBoard[7][7][0] , self.gameBoard[7][7][1] , "Black" ) ) ) )
        # Bishop_1_Black =    self.board[7].append ( Spot( 7*SQUARE, 6*SQUARE, (Bishop( self.gameBoard[7][6][0] , self.gameBoard[7][6][1] , "Black" ) ) ) )
        # Rook_1_Black =      self.board[7].append ( Spot( 7*SQUARE, 7*SQUARE, (Rook( self.gameBoard[7][5][0] , self.gameBoard[7][5][1] , "Black" ) ) ) )





























    # def resetBoard(self):
    #     #TODO: this assignement is fucked, I want it so that i can acces the Spot objects
    #     #TODO: find a way to store these Objects.
    #     #TODO: i need them for calculating moves and etc in the Game Class 
    #     #white 
    #     Spot( self.gameBoard[7][0] , self.gameBoard[0][1] , Rook.setWhite())
    #     Spot( self.gameBoard[7][0] , self.gameBoard[1][1] , Knight.setWhite())
    #     Spot( self.gameBoard[7][0] , self.gameBoard[2][1] , Bishop.setWhite())
    #     Spot( self.gameBoard[6][0] , self.gameBoard[0][1] , Pawn.setWhite())
    #     Spot( self.gameBoard[6][0] , self.gameBoard[1][1] , Pawn.setWhite())
    #     Spot( self.gameBoard[6][0] , self.gameBoard[2][1] , Pawn.setWhite())


    #     #black
    #     Spot( self.gameBoard[0][0] , self.gameBoard[0][1] , Rook)
    #     Spot( self.gameBoard[0][0] , self.gameBoard[1][1] , Knight)
    #     Spot( self.gameBoard[0][0] , self.gameBoard[2][1] , Bishop)
    #     Spot( self.gameBoard[1][0] , self.gameBoard[0][1] , Pawn)
    #     Spot( self.gameBoard[1][0] , self.gameBoard[1][1] , Pawn)
    #     Spot( self.gameBoard[1][0] , self.gameBoard[2][1] , Pawn)
    #     pass
        
    #     for i in range(2,6):
    #         for j in range(0, 8):
    #             Spot(self.gameBoard[j][0], self.gameBoard[i][1], None)