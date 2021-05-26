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
        #Black Peices  
        Rook_0_Black =   Rook( self.gameBoard[-8][0][0] ,  self.gameBoard[-8][0][1] ,  "Black" )        
        Bishop_0_Black = Bishop( self.gameBoard[-8][1][0] ,  self.gameBoard[-8][1][1] ,  "Black" )        
        Knight_0_Black = Knight( self.gameBoard[-8][2][0] ,  self.gameBoard[-8][2][1] ,  "Black" )        
        King_0_Black =   King( self.gameBoard[-8][3][0] ,  self.gameBoard[-8][3][1] ,  "Black" )        
        Queen_0_Black =  Queen( self.gameBoard[-8][4][0] ,  self.gameBoard[-8][4][1] ,  "Black" )        
        Knight_1_Black = Knight( self.gameBoard[-8][5][0] ,  self.gameBoard[-8][5][1] ,  "Black" )        
        Bishop_1_Black = Bishop( self.gameBoard[-8][6][0] ,  self.gameBoard[-8][6][1] ,  "Black" )        
        Rook_1_Black =   Rook( self.gameBoard[-8][7][0] ,  self.gameBoard[-8][7][1] ,  "Black" )

        wh_list = [
            Rook_0_Black,
            Bishop_0_Black,
            Knight_0_Black,
            King_0_Black,
            Queen_0_Black,
            Knight_1_Black,
            Bishop_1_Black,
            Rook_1_Black
        ]

        for i, x in enumerate(wh_list):
            x.draw(x.color, screen)
            self.board[7].append( Spot( 0*SQUARE, i*SQUARE, x ))

        Pawns = {}
        for i in range(0, BOARD_LENGTH):
            Pawns["p_"+str(i)+"_b"] = Pawn_ = Pawn( self.gameBoard[1][i][0], self.gameBoard[1][i][1], "Black")
            Pawn_.draw(Pawn_.color, screen)
            self.board[6].append( Spot( 1*SQUARE, i*SQUARE, Pawn_ ))


        #White Peices  
        Rook_0_White =   Rook( self.gameBoard[7][0][0] ,  self.gameBoard[7][0][1] ,  "White")
        Bishop_0_White = Bishop( self.gameBoard[7][1][0] ,  self.gameBoard[7][1][1] ,  "White")    
        Knight_0_White = Knight( self.gameBoard[7][2][0] ,  self.gameBoard[7][2][1] ,  "White")     
        King_0_White =   King( self.gameBoard[7][3][0] ,  self.gameBoard[7][3][1] ,  "White")    
        Queen_0_White =  Queen( self.gameBoard[7][4][0] ,  self.gameBoard[7][4][1] ,  "White")     
        Knight_1_White = Knight( self.gameBoard[7][5][0] ,  self.gameBoard[7][5][1] ,  "White")      
        Bishop_1_White = Bishop( self.gameBoard[7][6][0] ,  self.gameBoard[7][6][1] ,  "White")      
        Rook_1_White =   Rook( self.gameBoard[7][7][0] ,  self.gameBoard[7][7][1] ,  "White")

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

        
        for i in range(0, BOARD_LENGTH):
            Pawns["p_"+str(i)+"_w"] = Pawn_ = Pawn( self.gameBoard[-2][i][0], self.gameBoard[-2][i][1], "White")
            Pawn_.draw(Pawn_.color, screen)
            self.board[1].append( Spot( 1*SQUARE, i*SQUARE, Pawn_ ))
        empty = {}
        for i in range(2 , 6):
            for j in range(0, BOARD_LENGTH):
                empty[f"spot({j},{i})"] = Emp =Spot(j , i, piece=None)
                self.board[i].append(Emp)
