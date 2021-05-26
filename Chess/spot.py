class Spot:
    def __init__(self,x:int, y:int, piece:object) -> None:
        self.Piece = piece
        self.x = x
        self.y = y

    # #get pre-existing values for the spot
    # def get_Piece(self) -> str:
    #     return self.Peice
    # def get_X(self):
    #     return self.x
    # def get_Y(self):
    #     return self.x

    ## define new values for the spot 
    def setPeice(self, Piece):
        self.Piece = Piece
        pass
    def set_X(self, x:int):
        self.x = x
        pass
    def set_Y(self, y:int):
        self.x = y
        pass