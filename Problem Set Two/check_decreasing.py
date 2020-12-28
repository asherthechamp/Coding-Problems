# Checks if an array is in a decreasing order

def check(lst):
    largest = lst[0]
    found = 0

    for i in range(1, len(lst)):
        if(lst[i] >= largest):
            largest = lst[i]
        else:
            if(found > 1):
                return False
            else:
                found += 1
    return True

print (str(check([13, 4, 7])))
# True
print (str(check([5,1,3,2,5])))
# False