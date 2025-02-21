import random
import copy










#### MAIN OPERATIONAL FUNCTIONS ####
def transpose(matrix):
    for i in range(4):
        for j in range(i, 4):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
def flip(matrix):
    for i in range(4):
        for j in range(2):
            matrix[i][j], matrix[i][3-j] = matrix[i][3-j], matrix[i][j]
def side(matrix):
    for i in range(4):
        helper = 0
        for j in range(4):
            if matrix[i][j] != 0:
                matrix[i][j], matrix[i][helper] = matrix[i][helper], matrix[i][j]
                helper += 1
def compress(matrix):
    comp = False
    for i in range(4):
        for j in range(3):
            if matrix[i][j] != 0 and matrix[i][j] == matrix[i][j+1]:
                matrix[i][j] = 2 * matrix[i][j]
                matrix[i][j + 1] = 0
                comp = True
    return comp










#### DIRECTION FUNCTIONS ####
def left(matrix):
    helper = copy.deepcopy(matrix)
    side(matrix)
    comp = compress(matrix)
    side(matrix)
    return helper == matrix, comp
def up(matrix):
    helper = copy.deepcopy(matrix)
    transpose(matrix)
    side(matrix)
    comp = compress(matrix)
    side(matrix)
    transpose(matrix)
    return helper == matrix, comp
def right(matrix):
    helper = copy.deepcopy(matrix)
    flip(matrix)
    side(matrix)
    comp = compress(matrix)
    side(matrix)
    flip(matrix)
    return helper == matrix, comp
def down(matrix):
    helper = copy.deepcopy(matrix)
    transpose(matrix)
    flip(matrix)
    side(matrix)
    comp = compress(matrix)
    side(matrix)
    flip(matrix)
    transpose(matrix)
    return helper == matrix, comp










#### GAME STATUS ####
def check(matrix):
    for i in range(4):
        for j in range(4):
            if matrix[i][j] == 0:
                return True, True
    for i in range(4):
        for j in range(4):
            if i != 3 and j != 3:
                if matrix[i][j] == matrix[i][j+1] or matrix[i][j] == matrix[i+1][j]:
                    return True, False
            elif i != 3:
                if matrix[i][j] == matrix[i + 1][j]:
                    return True, False
            elif j != 3:
                if matrix[i][j] == matrix[i][j+1]:
                    return True, False
    return False, False
def win(matrix):
    for i in range(4):
        for j in range(4):
            if matrix[i][j] == 2048:
                return True
    return False











#### ADDING 2 AND 4 ####
def add():
    global matrix
    while True:
        x = random.randint(0, 3)
        y = random.randint(0, 3)
        if matrix[x][y] == 0:
            helper = random.choice([2, 4])
            matrix[x][y] = helper
            return [helper, x, y]










#### INITIAL MATRIX ####
matrix = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]










#### STARTING FUNCTION OR FUNCTION FOR GIVING ARRAY ####
def operator(direction):
    global matrix
    ad = False
    if direction == "start":
        matrix = [[0, 0, 0, 0],
                  [0, 0, 0, 0],
                  [0, 0, 0, 0],
                  [0, 0, 0, 0]]
        flag, comp = False, False
    elif direction == "left":
        flag, comp = left(matrix)
    elif direction == "up":
        flag, comp = up(matrix)
    elif direction == "right":
        flag, comp = right(matrix)
    elif direction == "down":
        flag, comp = down(matrix)

    ans = win(matrix)
    checking, adding = check(matrix)
    if checking:
        if adding and not flag:
            ad = True
        return [matrix, ad, comp, ans, True]
    else:
        return [matrix, ad, comp, ans, False]