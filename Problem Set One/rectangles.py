# Given a matrix of 0 and 1, return the number of rectangles that can be formed with 1s

def no_rectangle(matrix):
    points = {}
    count = 0
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            if matrix[i][j] == 1:
                points[len(points) + 1] = (i, j)
    rects = {}
    for p1 in points.values():
        for p2 in points.values():
            if is_rect(p1, p2, points) and (p1, p2) not in rects and (p2, p1) not in rects:
                rects[len(rects)+1] = (p1, p2)
                print(p1, p2)
                # count += 1
    return len(set(rects.values()))

def is_rect(p1, p2, points):

    starti = min(p1[0], p2[0])
    endi = max(p1[0], p2[0])
    for i in range(starti, endi +1):
        startj = min(p1[1], p2[1])
        endj = max(p1[1], p2[1])
        for j in range(startj, endj + 1):
            if (i, j) in points.values():
                continue
            else:
                return False
    return True

mat = [[0,1,1,0],
      [0,1,1,1],
      [1,1,1,0]]
print(no_rectangle(mat))