import pygame
from .constants import BLACK, BOARD_LENGTH, SQUARE, WHITE

class Piece():
    def __init__(self, col:int, row:int, color:str) -> None:
        self.killed = False
        self.color = color
        self.row = row
        self.col = col
        self.image = None
        self.name:str
        self.x:int
        self.y:int
        self.getPos()
        self.possible_moves = []
    
    def __repr__(self) -> str:
        return f"{self.color} {self.name} at ({self.col},{self.row})"

    def setWhite(self):
        self.white = True

    def isKilled(self):
        self.killed = True
        
    def getPos(self):
        self.x = self.col*SQUARE 
        self.y = self.row*SQUARE 

    def draw(self, color, screen):
        if self.image == None:
            color_ = "WHITE" if WHITE == color else "BLACk" 
            self.image = pygame.image.load(f"asset\\{self.name.upper()}_{color_.upper()}.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (80, 80))
        screen.blit(self.image, pygame.Rect(self.x+10, self.y+10, 100 ,10 ))
        pygame.display.update()

    def horizontal_moves(self,start,end,board):
        for i in range(start.col-1, -1, -1):
            spot = board[start.row][i]
            if spot.Piece == 0 or spot.Piece.color != self.color:
                self.possible_moves.append(spot)
                continue
            elif spot.Piece.color == self.color:
                break
        for i in range(start.col+1, BOARD_LENGTH):
            spot = board[start.row][i]
            if spot.Piece == 0 or spot.Piece.color != self.color:
                self.possible_moves.append(spot)
                continue
            elif spot.Piece.color == self.color:
                break
        ## Vertical movements of the piece
        for i in range(start.row+1, BOARD_LENGTH):
            spot = board[i][start.col]
            if spot.Piece == 0 or spot.Piece.color != self.color: 
                self.possible_moves.append(board[i][start.Piece.col])
                continue
            elif spot.Piece.color == self.color:
                break
        for i in range(start.row-1, -1,-1):
            spot = board[i][start.col]
            if spot.Piece == 0 or spot.Piece.color != self.color: 
                self.possible_moves.append(board[i][start.Piece.col])
                continue
            elif spot.Piece.color == self.color:
                break
        return self.possible_moves

    def diagonal_moves(self, col_row:tuple, board):
        _colrow = list(col_row)
        row = _colrow.pop()
        col ,= _colrow
        possible_moves = []
        directions = [[1,1],[-1,1],[1,-1],[-1,-1]]
        for dir in directions:
            d1,d2 = dir
            for x,j in enumerate(range(1,BOARD_LENGTH),1):
                if 0 <= col + (x)*d1 < BOARD_LENGTH and 0 <= (j)*d2 + row < BOARD_LENGTH: 
                    spot = board[ row + (j*d2)][col + (x*d1)]
                    print(spot)
                    if spot.Piece == 0:
                        possible_moves.append(spot)
                    else:
                        if spot.Piece.color != self.color:
                            possible_moves.append(spot)
                            break
                        break
                else:
                    break
        self.possible_moves += list(set(possible_moves))
        return self.possible_moves


class King(Piece):
    def __init__(self,col,row,color) -> None:
        super(King, self).__init__(col,row,color)
        self.isCastled = False
        self.name = "King"
    
    def canMove(self, start:object, end:object, board:object) -> bool:
        # TODO: write the conditions for a stalements and what not 
        if end.Piece:
            if end.Piece.color == self.color:
                return False
        else: 
            y = abs(end.y - start.y)
            x = abs(end.x - start.x)
            moves = [(1,1),(1,0),(0,1)]
            if (x,y) in moves: 
                return True
        return False
    def isValidCastle(self, Board, start, end) -> bool:
        # TODO: write the logic for checking castling here
        pass


    def Castle(self, start, end) -> None:
        # TODO: write the logic for performing a castling here
        pass
    

    
class Queen(Piece):
    def __init__(self,col,row,color) -> None:
        super(Queen, self).__init__(col,row,color)
        self.name = "Queen"

    def canMove(self, start:object, end:object, board:object) -> bool:
        self.possible_moves = []
        self.possible_moves += self.horizontal_moves(start,end,board)
        self.possible_moves += self.diagonal_moves((start.col,start.row),board)
        if end in self.possible_moves:
            return True
        return False

        


class Knight(Piece):
    def __init__(self,col,row,color) -> None:
        super(Knight, self).__init__(col,row,color)
        self.name = "Knight"

    def canMove(self, start:object, end:object, board:object):
        x = abs(start.col - end.col)
        y = abs(start.row - end.row)
        print(x)
        print(y)
        def possible():
            if board[end.row][end.col].Piece == 0:
                return True 
            elif  board[end.row][end.col].Piece.color != self.color:
                return True
            else:
                return False
        if x == 2 and y == 1:
            return possible()
        elif x==1 and y==2:
            return possible()
        return False



class Bishop(Piece):
    def __init__(self,col,row,color) -> None:
        super(Bishop, self).__init__(col,row,color)
        self.name = "Bishop"

    def endLoop(self) -> StopIteration:
        raise StopIteration

    def canMove(self, start:object, end:object, board:object):
        self.possible_moves = []
        start_spot = (start.col, start.row)
        self.possible_moves += self.diagonal_moves(start_spot,board)
        if end in self.possible_moves:
            return True 
        return False


  

class Rook(Piece):
    def __init__(self,col,row,color) -> None:
        super(Rook, self).__init__(col,row,color)
        self.name = "Rook"
        

    def canMove(self, start:object, end:object, board:object):
        self.possible_moves = []
        ## Horizontal movements of the piece 
        self.possible_moves += self.horizontal_moves(start,end,board)
        if end in set(self.possible_moves):
            print(set(self.possible_moves))
            return True
        return False

class Pawn(Piece):
    def __init__(self, col,row, color) -> None:
        super(Pawn, self).__init__(col,row,color)
        self.name = "Pawn"
        self.firstMove = True
        self.promoted = False
    
    def first(self):
        self.firstMove = False
        pass

    def promoteQueen(self):
        self.promoted = True
        self.name = "Queen"
        self.draw()

    def canMove(self, start:object, end:object, board):
        y  = end.row - start.row
        x = end.col - start.col
        direction = 1 if self.color == BLACK else -1
        if not self.promoted:
            if (x == 1 or x == -1) and y == direction:
                if end.Piece.color != self.color:
                    return True
                else: return False
            if x == 0:
                if self.firstMove == True:
                    if end.Piece:
                        return False
                    elif y <= 2 :
                        self.firstMove = False
                        return True
                return True if y == direction and end.Piece == 0 else False       
        else:
            self.possible_moves = []
            self.possible_moves += self.horizontal_moves(start,end,board)
            self.possible_moves += self.diagonal_moves((start.col,start.row),board)
            if end in self.possible_moves:
                return True
            return False


