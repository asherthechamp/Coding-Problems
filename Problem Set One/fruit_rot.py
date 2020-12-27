# Calculates the time it takes for all fruits to rot

def fruit_rot(array):
    count = 0
    while 1:
        has_rotten = False
        has_fresh = False
        i = 0
        while i < len(array):
            j = 0
            inc_i = False
            while j < len(array[0]):
                if array[i][j] == 1:
                    has_fresh = True
                if array[i][j] == 2:
                    if j - 1 >= 0 and array[i][j-1] == 1:
                        array[i][j-1] = 2
                        has_rotten = True
                    if j + 1 < len(array[0]) and array[i][j+1] == 1:
                        array[i][j+1] = 2
                        has_rotten = True
                        j += 1
                    if i - 1 >= 0 and array[i-1][j] == 1:
                        array[i-1][j] = 2
                        has_rotten = True
                    if i + 1 < len(array) and array[i+1][j] == 1:
                        array[i+1][j] = 2
                        has_rotten = True
                        inc_i = True
                j += 1
            if inc_i:
                i += 2
            else:
                i += 1
        if not has_rotten:
            if has_fresh:
                return -1
            else:
                return count
        count += 1

print(fruit_rot([[0,2]]))



