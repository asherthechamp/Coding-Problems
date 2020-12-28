# Returns if the next witness is taller than the current person

def witness(heights):
    talls = []
    for i in range(0, len(heights)):
        if i == len(heights) - 1:
            talls.append(heights[i])
        else:
            if heights[i] > heights[i+1]:
                talls.append(heights[i])
    return len(talls)

print(witness([3, 6, 3, 4, 1] ))