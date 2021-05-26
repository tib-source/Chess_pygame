class Game:

    def __init__(self, p1:object, p2:object, board) -> None:
        self.Board = board
        self.playedMoves = []
        self.turn = 0
        self.players = [p1, p2] 
        self.gameOver = False

    def create(self, Board:object):
        Board.resetBoard()

    def addMove(self, player, start, end):
        
        pass
    def isEnded(self):
        self.gameOver = True
        pass
    def isChecked(self):
        pass
    def operation(self):
        pass
    def isCheckmated(self):
        pass