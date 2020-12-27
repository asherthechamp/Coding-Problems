# Calculates the maximum distance between occupied seats

def max_distance(seats):
    dist_dict = {}
    x = 0
    y = 0
    for i in range(0, len(seats)):
        if seats[i] == 1:
            y = i
            dist = y - x
            dist_dict[x-y] = (x, y)
            x = y
    sorted_dict = sorted(dist_dict.items(), key = lambda d: (d[0]), reverse = True)
    mid = sorted_dict[0][1] - sorted_dict[0][0] // 2
    return sorted_dict[0][1] + mid


