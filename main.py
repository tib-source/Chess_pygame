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





# class Move:
#     def __init__(self, Player:object, start:object, end:object) -> None:
#         self.Player = Player
#         self.start = start 
#         self.end = end 
#         self.PieceMoved: object
#         self.PieceKilled: object
#         self.castilingMove = False
    
#     def changePos(self):
#         if not self.castilingMove:
#             if self.start.Peice.canMove:
#                 self.start.Piece, self.end.Piece = self.start.Piece
#         pass
    


    #TODO : FINISH THIS CLASS


# Pygame GUI 
def main():
    #initialise the pygame module here   
    pygame.init()

    size = (WIDTH,HEIGHT)
    screen = pygame.display.set_mode(size)
    screen.fill(BLACK)

    clock = pygame.time.Clock()

    board = Board()
    board.drawBoard(screen)
    board.create_board(screen)
    pprint.pprint(board.gameBoard)
    
    run = True
    board.move( start=board.board[1][4], end=board.board[2][4], screen=screen)
    pygame.display.flip()
    ###
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()