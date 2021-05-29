from Chess.game import Game
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
def get_cr(pos):
    """ takes in a x and y value and returns the col and row that correspond to that """
    col = pos[0]//SQUARE
    row = pos[1]//SQUARE
    return col,row

# Pygame GUI 
def main():
    #initialise the pygame module here   
    pygame.init()

    size = (WIDTH,HEIGHT)
    screen = pygame.display.set_mode(size)
    screen.fill(BLACK)
    pygame.display.set_caption('Chess')
    clock = pygame.time.Clock()

    game = Game(screen)
    game.create()
    pprint.pprint(game.board.gameBoard)
    run = True
    ###
    selected = ()
    clicks = []
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if get_cr(pygame.mouse.get_pos()) == selected: # this checks to see if the same square has been pressed twice by the user
                    selected = ()
                    clicks = []
                else:
                    selected = get_cr(pygame.mouse.get_pos())
                    clicks.append(selected)
                if len(clicks) == 2:
                    start = game.board.getSpot(clicks[0])
                    end = game.board.getSpot(clicks[1])
                    game.board.move(start,end, game.screen)
                    print(start.Piece)
                    print(end.Piece) 
                    selected = ()
                    clicks = []





                # start = game.board.getSpot(get_cr(selected))

    pygame.quit()

if __name__ == "__main__":
    main()