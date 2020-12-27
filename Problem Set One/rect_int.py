# Given bottom left and top right points of two rectangles,
# check if the rectangles intersect

def rect_intrs(rect1, rect2):
    if (rect2[0] in range(rect1[0], rect1[2]) \
            or rect2[2] in range(rect1[0] + 1, rect1[2]) ) \
            and (rect2[1] in range(rect1[1] + 1, rect1[3]) \
            or rect2[3] in range(rect1[1] + 1, rect1[3]) ):
        return True
    else:
        return False

print (rect_intrs([5,15,8,18], [0,3,7,9]))
print(rect_intrs([0, 0, 1, 1], [2, 2, 3, 3]))
print (rect_intrs([0,0,1,1], [1,0,2,1]))
print (rect_intrs([0,0,2,2], [1,1,3,3]))
