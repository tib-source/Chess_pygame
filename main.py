from Chess.board import Board
import pygame
from Chess.constants import *
import pprint
# Game Logic

"""
Currently im thinking of not making a function that moves the peices inside the object class of the peice.
Instead, ill create an object for every single spot and for them give them a setPiece fucntion>
later on i can check a move of a peice with the "canMove" and the use the end.setPiece to complete it 

"""





class Move:
    def __init__(self, Player:object, start:object, end:object) -> None:
        self.Player = Player
        self.start = start 
        self.end = end 
        self.PieceMoved: object
        self.PieceKilled: object
        self.castilingMove = False
    
    def changePos(self):
        if not self.castilingMove:
            if self.start.Peice.canMove:
                self.PieceKilled = self.end.Peice if self.end.Peice else None
                self.start.Piece, self.end.Piece = self.start.Piece
        pass
    


    #TODO : FINISH THIS CLASS


# Pygame GUI 
def main():
    #initialise the pygame module here   
    pygame.init()

    size = (WIDTH,HEIGHT)
    screen = pygame.display.set_mode(size)
    screen.fill(BLACK)
    board = Board()
    board.drawBoard(screen)
    board.create_board(screen)
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(board.board)
    pp.pprint(board.board[0][1].x)
    pp.pprint(board.board[0][1].y)
    pygame.display.flip()
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()