import pygame
from .constants import BLACK, BOARD_LENGTH, SQUARE, WHITE

class Piece():
    def __init__(self, col:int, row:int, color:str) -> None:
        self.killed = False
        self.color = color
        self.row = int(row)
        self.col = int(col)
        self.image = None
        self.name:str
        self.x:int
        self.y:int
        self.pos = (self.col,self.row)
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
        try:
            if self.promoted:
                color_ = "WHITE" if WHITE == color else "BLACk" 
                self.image = pygame.image.load(f"asset\\{self.name.upper()}_{color_.upper()}.png").convert_alpha()
                self.image = pygame.transform.scale(self.image, (80, 80))
                screen.blit(self.image, pygame.Rect(self.x+10, self.y+10, 100 ,10 ))
                pygame.display.update()

        except:
            pass
        
        if self.image == None:
            color_ = "WHITE" if WHITE == color else "BLACk" 
            self.image = pygame.image.load(f"asset\\{self.name.upper()}_{color_.upper()}.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (80, 80))
        screen.blit(self.image, pygame.Rect(self.x+10, self.y+10, 100 ,10 ))
        pygame.display.update()

    def horizontal_moves(self,start,board):
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
        self.moved = False
        self.number_of_moves = 0

    def get_valid_moves(self,start,board):
        return ["HELLO"]

    def canMove(self, start:object, end:object, board:object) -> bool:
        # TODO: write the conditions for a stalements and what not #
        """
        TODO: need to add code that checks if move is a castle attempt then run the isValidCastle function 
        """
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

    def isValidCastle(self, board, start, end, rook_pk: int) -> bool:
        # TODO: write the logic for checking castling here
        
        """
        root_pk is a number either 0 or 1 that identifies which rook is being targeted for castle

        first - function should check wheather or not castle has already been made
        then check if the king had moved before this or if the king is in check - if so, return False 
        then check if the rook had moved before this - if so, return False 
        Check if there are any pieces between the two - if so, return False 
        if all the above conditions pass - return True
        
        official requirements for a castle 

        Castling is permissible provided all of the following conditions hold:[4]
            The castling must be kingside or queenside.[5]
            Neither the king nor the chosen rook has previously moved.
            There are no pieces between the king and the chosen rook.
            The king is not currently in check.
            The king does not pass through a square that is attacked by an enemy piece.
            The king does not end up in check. (True of any legal move.)

        source: https://en.wikipedia.org/wiki/Castling#Requirements
        
        """
        if not self.isCastled: 
            rooks = self.get_rooks()
            rook = rooks[rook_pk]
            if self.number_of_moves == rook.number_of_moves == 0 :
                #check for other peices between
                pass
        pass


    def castle(self, start, end) -> None:
        # TODO: write the logic for performing a castling here
        pass
    
    def get_rooks(self, board):
        color = self.color
        color_str = 'Black 'if color == BLACK else 'WHITE'
        num = ['0', '1']
        rooks = []
        for i in num: 
            rook_name = f"board.Rook_{i}_{color_str}"
            rook = exec(rook_name)
            rooks.append(rook)
        return rooks



    
class Queen(Piece):
    def __init__(self,col,row,color) -> None:
        super(Queen, self).__init__(col,row,color)
        self.name = "Queen"

    def get_valid_moves(self,start,board):
        self.possible_moves = []
        self.possible_moves += self.horizontal_moves(start,board)
        self.possible_moves += self.diagonal_moves((start.col,start.row),board)

    def canMove(self, start:object, end:object, board:object) -> bool:
        self.get_valid_moves(start,board)
        if end in self.possible_moves:
            return True
        return False

        


class Knight(Piece):
    def __init__(self,col,row,color) -> None:
        super(Knight, self).__init__(col,row,color)
        self.name = "Knight"
    def get_valid_moves(self,start,end):
        return ["HELLO"]
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
    
    def get_valid_moves(self, start, board):
        self.possible_moves = []
        start_spot = (start.col, start.row)
        self.possible_moves += self.diagonal_moves(start_spot,board)

    def canMove(self, start:object ,end:object, board:object):
        self.get_valid_moves(start, board)
        if end in self.possible_moves:
            return True 
        return False


  

class Rook(Piece):
    def __init__(self,col,row,color) -> None:
        super(Rook, self).__init__(col,row,color)
        self.name = "Rook"
        self.number_of_moves = 0
        
    def get_valid_moves(self,start,board):
        self.possible_moves = []
        ## Horizontal movements of the piece 
        self.possible_moves += self.horizontal_moves(start,board)

    def canMove(self, start:object, end:object, board:object):
        self.get_valid_moves(start,board)
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
    
    def get_valid_moves(self,start,board):
        self.possible_moves = []
        self.possible_moves += [(0,0)]
    def first(self):
        self.firstMove = False
        pass

    def promoteQueen(self):
        self.promoted = True
        self.name = "Queen"

    def canMove(self, start:object, end:object, board):
        y  = end.row - start.row
        x = end.col - start.col
        direction = 1 if self.color == BLACK else -1
        final_row = 7 if self.color == BLACK else 0
        if not self.promoted:
            if (x == 1 or x == -1) and y == direction:
                if end.Piece == 0:
                    return False 
                if end.Piece.color != self.color:
                    if end.Piece.row == final_row:
                        self.promoteQueen()
                    return True
                else:
                    return False
            if x == 0:
                if self.firstMove == True:
                    if end.Piece:
                        return False
                    elif y <= 2 :
                        self.firstMove = False
                        return True
                if y == direction and end.Piece == 0:
                    if end.row == final_row:
                        self.promoteQueen()
                    return True
                else: return False       
        else:
            self.possible_moves = []
            self.possible_moves += self.horizontal_moves(start,board)
            self.possible_moves += self.diagonal_moves((start.col,start.row),board)
            if end in self.possible_moves:
                return True
            return False


