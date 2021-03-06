from Chess.constants import ROWS, SQUARE, WHITE, BLACK


class Spot:
    def __init__(self,x:int, y:int, piece:object) :
        self.Piece = piece
        self.x = x
        self.y = y
        self.col = x//SQUARE
        self.row = y//SQUARE
        self.pos = (self.col,self.row)
        self.mod = (self.col + self.row)%2
        if self.mod == 0:
            self.color = WHITE
        else:
            self.color = BLACK
    # #get pre-existing values for the spot
    def get_Piece(self):
        return self.Peice
    # def get_X(self):
    #   return self.x
    # def get_Y(self):
    #     return self.x

    ## define new values for the spot 
    def setPeice(self, piece):
        self.Piece = piece
        
    def set_X(self, x:int):
        self.x = x
        
    def set_Y(self, y:int):
        self.x = y
        
    def __repr__(self) -> str:
        return f"Spot at ({self.col},{self.row})"

