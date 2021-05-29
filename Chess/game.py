from Chess.constants import BLACK, BOARD_LENGTH, WHITE
from .board import Board
import pygame

class Game:

    def __init__(self, screen) -> None:
        self.screen = screen
        self._init()
        self.board.drawBoard(self.screen)

    def create(self):
        self.board.create_board(self.screen)
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.playedMoves = []
        self.turn = WHITE
        self.gameOver = False
        self.valid_moves = []

    def reset(self):
        self._init()
    def isEnded(self):
        self.gameOver = True
        pass
    def isChecked(self):
        pass
    def operation(self):
        pass
    def isCheckmated(self):
        pass
    def get_valid_moves(self,Piece):
        self.valid_moves = [[ (i,j) for i in range(BOARD_LENGTH) if Piece.canMove(i,self.board[j][i]) ] for j in range(BOARD_LENGTH)]

    def select(self,col,row):
        if self.selected:
            result = self._move(col,row)
            if not result:
                self.selected = None
                self.select(col,row)
        spot = self.board.getSpot([col,row])
        if spot.Piece != 0 and spot.Piece.color == self.turn:
            self.selected = spot
            self.valid_moves = self.get_valid_moves(spot.Piece)
            return True

        return False        

    def _move(self,col,row):
        spot = self.board.getSpot([col,row])
        if self.selected and spot.Piece == 0 and (row,col) in self.valid_moves:
            self.board.move(self.selected, spot)
        else:
            return False
        return True

    def changeTurn(self): 
        if self.turn == WHITE:
            self.turn = BLACK
        else:
            self.turn = WHITE