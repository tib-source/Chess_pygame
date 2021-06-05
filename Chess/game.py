from Chess.peice import King
from Chess.constants import BLACK, BOARD_LENGTH, WHITE,SQUARE
from .board import Board
import pygame
import pprint

class Game:
    # chess_notation= {
    #     "a": 1,
    #     "b": 2,
    #     "c": 3,
    #     "d": 4,
    #     "e": 5,
    #     "f": 6,
    #     "g": 7,
    #     "h": 8
    #     "B": ,
    #     "B": ,
    #     "B": ,
    #     "B": ,
    #     "B": ,
    # }
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
        self.gBoard = self.board.board

    def reset(self):
        self._init()

    def isEnded(self):
        self.gameOver = True
        pass
    

    ### TODO: This function need to be really fast so threading should probably be added
    def isChecked(self):
        self.Moves = {}
        king = self.board.King_0_Black if self.turn == BLACK else self.board.King_0_WHITE
        king_spot = self.board.getSpot(king.pos)
        self.friend_mov = {}
        print(king)
        for y in range(BOARD_LENGTH):
            for x in self.gBoard[y]:
                if x.Piece == 0: continue
                if x.Piece.color != king.color: 
                    x.Piece.get_valid_moves(x,self.gBoard)
                    self.Moves[x] = set(x.Piece.possible_moves)
                else:
                    x.Piece.get_valid_moves(x,self.gBoard)
                    self.friend_mov[x] = x.Piece.possible_moves

        possible = set().union(*self.Moves.values())
        print(f"ENEMY MOVES {self.Moves}")
        print("\n")
        print(f"Friendly Moves {self.friend_mov} " )
        print("\n")
        print(king.pos)
        print(f"possible movement of enemies: {possible}")
        if king_spot in possible:
            print(f" X IS {x}")
            print(f" KING POSITION IS {king.pos}")
            print(
                    """
    ┈┈╭━╱▔▔▔▔╲━╮┈┈┈
    ┈┈╰╱╭▅╮╭▅╮╲╯┈┈┈
    ╳┈┈▏╰┈▅▅┈╯▕┈┈┈┈
    ┈┈┈╲┈╰━━╯┈╱┈┈╳┈
    ┈┈┈╱╱▔╲╱▔╲╲┈┈┈┈
    ┈╭━╮▔▏┊┊▕▔╭━╮┈╳
    ┈┃┊┣▔╲┊┊╱▔┫┊┃┈┈
    ┈╰━━━━╲╱━━━━╯┈╳
                    """
                
                )
            return True
        return False

    def operation(self):
        pass

    def isCheckmated(self):
        return self.gameOver == False

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

    def move(self, start, end, screen) -> None:
        if start.Piece.canMove(start,end,self.gBoard):
            end.Piece, start.Piece = start.Piece, end.Piece
            end.Piece.col, end.Piece.row  = end.col,end.row 
            pygame.draw.rect(screen, start.color , pygame.Rect(start.x,start.y,SQUARE,SQUARE))
            pygame.draw.rect(screen, end.color , pygame.Rect(end.x,end.y,SQUARE,SQUARE))
            end.Piece.getPos()
            end.Piece.draw(end.Piece.color, screen)
            pygame.display.update()
            self.playedMoves.insert(0, f"{end.Piece.name}: {start.pos} -> {end.pos}") ### TODO: REWRITE THIS SO THAT IT ADDS THE MOVEMENT OF THE CHESS PIECES IN ACTUAL CHESS NOTATION INSTEAD
            return True
        else:
            return False