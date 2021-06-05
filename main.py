from pygame.constants import KEYDOWN
from Chess.game import Game
from Chess.board import Board
import pygame
from Chess.constants import *
from time import sleep
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



    while not game.gameOver:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == KEYDOWN:
                if event.key == pygame.K_r:
                    print("Resetting game ... ")
                    sleep(1)
                    main()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if get_cr(pygame.mouse.get_pos()) == selected: # this checks to see if the same square has been pressed twice by the user
                    clicks.clear()
                    selected = ()
                else:
                    selected = get_cr(pygame.mouse.get_pos())
                    clicks.append(selected)

                if len(clicks) == 2:
                    print(f"TURN {game.turn}")
                    start = game.board.getSpot(clicks[0])
                    end = game.board.getSpot(clicks[1])
                    if start.Piece == 0 or start == end:
                        clicks.clear()
                        selected = ()    
                        continue
                    elif start.Piece.color == game.turn:
                        if not game.isChecked():
                            if game.move(start,end, game.screen):
                                game.changeTurn()
                                print(f"TURN CHANGED TO {game.turn}")
                            else:
                                print('Invalid Move','This peice cant move there')
                                print(start.pos, end.pos)
                                clicks.clear()
                                selected = ()
                                continue
                        else:
                            print("THE PLAY IS IN CHECKKKK ")
                    else:
                        print("Wrong Trun", 'It is not your turn right now')
                    clicks.clear()
                    selected = ()

                # start = game.board.getSpot(get_cr(selected))

    pygame.quit()

if __name__ == "__main__":
    main()


"""


[
 [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)],
 [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)],
 [(0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2)],
 [(0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3)],
 [(0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4)],
 [(0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5)],
 [(0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)],
 [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7)]
]



"""