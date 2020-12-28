# returns the flipped (from right to left of a raw) and inverted (0 becomes 1 and 1 becomes 0) image of a strign

def flipAndInvertImage(A: list[list[int]]) -> list[list[int]]:
    new_array = []
    newest_array = []
    for arr1 in A:
        new_array.append(arr1[::-1])
    for arr2 in new_array:
        newer_array = []
        for i in arr2:
            newer_array.append(1 - i)
        newest_array.append(newer_array)
    return newest_array

def another_one(A):
    for l in range(0, len(A)):
        A[l] = A[l][::-1]
    for i in range(0, len(A)):
        for j in range(0, len(A[i])):
            A[i][j] = 1 - A[i][j]

    return A

print(another_one([[1,1,0],[1,0,1],[0,0,0]]))
#print(flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))