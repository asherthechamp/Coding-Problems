# Takes a matrix and returns antother matrix with the distance it takes to an adjacent zero

def matrix_distance(matrix):
    new_matrix = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
    for l in range(0, len(matrix)):
        for m in range(0, len(matrix[0])):
            new_matrix[l][m] = calculate_distance(matrix, (l, m))
    return new_matrix

def calculate_distance(matrix, tuple):
    if matrix[tuple[0]][tuple[1]] == 0:
        return 0
    right = move_right(tuple, matrix)
    left = move_left(tuple, matrix)
    up = move_up(tuple, matrix)
    down = move_down(tuple, matrix)
    return min(right, left, up, down)

def move_right(tuple, matrix):
    g = tuple[0]
    h = tuple[1] + 1
    distance = 0
    found = False
    distance = 1
    while 1 and h < len(matrix[0]):
        if matrix[g][h] == 0:
            found = True
            break
        else:
            distance += 1
            h += 1
    if found:
        return distance
    else:
        return float('inf')

def move_left(tuple, matrix):
    g = tuple[0]
    h = tuple[1] - 1
    distance = 0
    found = False
    distance = 1
    while 1 and h >= 0:
        if matrix[g][h] == 0:
            found = True
            break
        else:
            distance += 1
            h -= 1
    if found:
        return distance
    else:
        return float('inf')

def move_up(tuple, matrix):
    g = tuple[0] - 1
    h = tuple[1]
    distance = 0
    found = False
    distance = 1
    while 1 and g >= 0:
        if matrix[g][h] == 0:
            found = True
            break
        else:
            distance += 1
            g -= 1
    if found:
        return distance
    else:
        return float('inf')

def move_down(tuple, matrix):
    g = tuple[0] + 1
    h = tuple[1]
    distance = 0
    found = False
    distance = 1
    while 1 and g < len(matrix):
        if matrix[g][h] == 0:
            found = True
            break
        else:
            distance += 1
            g += 1
    if found:
        return distance
    else:
        return float('inf')

# matrix = [[0,0,0],
#  [0,1,0],
#  [0,0,0]]

matrix = [[0,0,0],
 [0,1,0],
 [1,1,1]]

print(matrix_distance(matrix))