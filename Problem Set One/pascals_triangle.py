# Returns the pascals triangle

def pascals(n):
    result = [[1]]

    for i in range(1, n):
        array = []
        for j in range(0, i + 1):
            if j-1 >= 0 and j <= i - 1:
                array.append(result[i-1][j - 1] + result[i-1][j])
            elif j-1 < 0:
                array.append(0 + result[i-1][j])
            elif j > i -1:
                array.append(result[i-1][j - 1] + 0)
        result .append(array)
    return result

print(pascals(5))