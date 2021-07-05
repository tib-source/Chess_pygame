import pygame
from .peice import *
from .spot import Spot
from .constants import (
    BLACK,
    BOARD_LENGTH,
    WHITE,
    SQUARE,
)


class Board:
    def __init__(self) -> None:
        self.board = [[] for _ in range(8)]
        self.gameBoard = [[(col , row) for col in range(0, BOARD_LENGTH)]for row in range(0, BOARD_LENGTH)]
        
#TODO: Make a constant for the initial rows and cols of the peices
    def getSpot(self,pos):
        col , row = pos
        return self.board[row][col]
        
    def drawBoard(self,screen):
        for x in range(BOARD_LENGTH):
            for y in range(x%2,BOARD_LENGTH,2):
                pygame.draw.rect(screen, WHITE, pygame.Rect(x*SQUARE,y*SQUARE,SQUARE,SQUARE))

    def create_board(self,screen):
        #Black Peices  
        self.Rook_0_Black =   Rook( self.gameBoard[-8][0][0] ,  self.gameBoard[-8][0][1] ,  BLACK )        
        self.Bishop_0_Black = Bishop( self.gameBoard[-8][1][0] ,  self.gameBoard[-8][1][1] ,  BLACK )        
        self.Knight_0_Black = Knight( self.gameBoard[-8][2][0] ,  self.gameBoard[-8][2][1] ,  BLACK )        
        self.King_0_Black =  King( self.gameBoard[-8][4][0] ,  self.gameBoard[-8][4][1] ,  BLACK )        
        self.Queen_0_Black =  Queen( self.gameBoard[-8][3][0] ,  self.gameBoard[-8][3][1] ,  BLACK )        
        self.Knight_1_Black = Knight( self.gameBoard[-8][5][0] ,  self.gameBoard[-8][5][1] ,  BLACK )        
        self.Bishop_1_Black = Bishop( self.gameBoard[-8][6][0] ,  self.gameBoard[-8][6][1] ,  BLACK )        
        self.Rook_1_Black =   Rook( self.gameBoard[-8][7][0] ,  self.gameBoard[-8][7][1] ,  BLACK )

        wh_list = [
            self.Rook_0_Black,
            self.Bishop_0_Black,
            self.Knight_0_Black,
            self.Queen_0_Black,
            self.King_0_Black,
            self.Knight_1_Black,
            self.Bishop_1_Black,
            self.Rook_1_Black
        ]

        for i, x in enumerate(wh_list):
            x.draw(x.color, screen)
            self.board[0].append( Spot( i*SQUARE, 0*SQUARE, x ))

        Pawns = {}
        for i in range(0, BOARD_LENGTH):
            Pawns["p_"+str(i)+"_b"] = Pawn_ = Pawn( self.gameBoard[1][i][0], self.gameBoard[1][i][1], BLACK)
            Pawn_.draw(Pawn_.color, screen)
            self.board[1].append( Spot( i*SQUARE, 1*SQUARE, Pawn_ ))


        #WHITE Peices  
        self.Rook_0_WHITE =   Rook( self.gameBoard[7][0][0] ,  self.gameBoard[7][0][1] ,  WHITE)
        self.Bishop_0_WHITE = Bishop( self.gameBoard[7][1][0] ,  self.gameBoard[7][1][1] ,  WHITE)    
        self.Knight_0_WHITE = Knight( self.gameBoard[7][2][0] ,  self.gameBoard[7][2][1] ,  WHITE)     
        self.Queen_0_WHITE =   Queen( self.gameBoard[7][3][0] ,  self.gameBoard[7][3][1] ,  WHITE)    
        self.King_0_WHITE =  King( self.gameBoard[7][4][0] ,  self.gameBoard[7][4][1] ,  WHITE)     
        self.Knight_1_WHITE = Knight( self.gameBoard[7][5][0] ,  self.gameBoard[7][5][1] ,  WHITE)      
        self.Bishop_1_WHITE = Bishop( self.gameBoard[7][6][0] ,  self.gameBoard[7][6][1] ,  WHITE)      
        self.Rook_1_WHITE =   Rook( self.gameBoard[7][7][0] ,  self.gameBoard[7][7][1] ,  WHITE)

        wh_list = [
            self.Rook_0_WHITE,
            self.Bishop_0_WHITE,
            self.Knight_0_WHITE,
            self.Queen_0_WHITE,
            self.King_0_WHITE,
            self.Knight_1_WHITE,
            self.Bishop_1_WHITE,
            self.Rook_1_WHITE
        ]

        for i, x in enumerate(wh_list):
            x.draw(x.color, screen)
            self.board[7].append( Spot( i*SQUARE, 7*SQUARE, x ))

        
        for i in range(0, BOARD_LENGTH):
            Pawns["p_"+str(i)+"_w"] = Pawn_ = Pawn( self.gameBoard[-2][i][0], self.gameBoard[-2][i][1], WHITE)
            Pawn_.draw(Pawn_.color, screen)
            self.board[6].append( Spot( i*SQUARE, 6*SQUARE, Pawn_ ))

        empty = {}
        for i in range(2 , 6):
            for j in range(0, BOARD_LENGTH):
                empty[f"spot({j},{i})"] = Emp = Spot(j*SQUARE , i*SQUARE, piece=0)
                self.board[i].append(Emp)





"""

Checkmate logic:
    check the movement of all the other pieces in the whole board 
    check if pieces 


"""