

WIDTH = 800
HEIGHT = 800
BOARD_LENGTH = ROWS = COLS = 8
SQUARE = WIDTH//ROWS

#FPS 
FPS = 60

#Colour (r,g,b)
BLACK = (23,24,59)
WHITE = (242,229,215)
BACK_COLOR = (201,237,220)


#Path
ASSETS_DIR= "..\\assets"

gameBoard = [
 [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)],
 [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)],
 [(0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2)],
 [(0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3)],
 [(0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4)],
 [(0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5)],
 [(0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)],
 [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7)]
]

def getDiagonal(col_row):
    _colrow = list(col_row)
    row = _colrow.pop()
    col ,= _colrow
    possible_moves = []
    directions = [[1,1],[-1,1],[1,-1],[-1,-1]]
    for dir in directions:
        d2 = dir.pop()
        d1 ,= dir 
        moves = [gameBoard[row + (j)*d2][(x)*d1 + col] for x,j in enumerate(range(BOARD_LENGTH)) if 0 <= col + (x)*d1 < BOARD_LENGTH and 0 <= (j)*d2 + row < BOARD_LENGTH]
        possible_moves += moves
    return set(possible_moves)


print(list(getDiagonal((6,0))))

