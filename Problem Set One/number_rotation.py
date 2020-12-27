# Given a digits and their rotation digits, return how many valid rotations can be done

def number_rotation(n):
    map_dict = {0:0, 1:1, 8:8, 2:5, 5:2, 6:9 , 9:6}
    rotn = ""
    for c in str(n):
        if c in map_dict.keys():
            rotc = map_dict[c]
            rotn += rotc
        else:
            return None
    return rotn

def num_of_valid_rot(N):
    count = 0
    for i in range (0, N+1):
        if number_rotation(i) and number_rotation(i) != i:
            count += 1
    return count






