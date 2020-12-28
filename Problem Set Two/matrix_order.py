# Retruns a sorted matrix from left to right and top to bottom

class Solution:
    def diagonalSort(self, mat: list[list[int]]) -> list[list[int]]:
        merged_array = []
        for i in range(0, len(mat)):
            merged_array += mat[i]
        merged_array.sort()
        print(len(merged_array))
        new_mat = [[None]*4, [None]*4, [None]*4]
        for x in range(0, len(mat)):
            for y in range(0, len(mat[x])):
                print(y + x*len(mat[x]))
                new_mat[x][y] = merged_array[y + x*len(mat[x])]
        return new_mat

print(Solution().diagonalSort([[3,3,1,1],[2,2,1,2],[1,1,1,2]]))