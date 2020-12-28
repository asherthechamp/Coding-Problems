# Binary Search Tree

class Solution:
    arr = []
    target = None
    def __init__(self, array, target_number):
        self.arr = array
        self.target = target_number
    def get_range(self, index):
        i = index
        while (i - 1 > 0 and self.arr[i - 1] == self.target):
            i -= 1
        first_index = i
        j = index
        while (j + 1 < len(self.arr) and self.arr[j + 1] == self.target):
            j += 1
        last_index = j
        return str(first_index) + str(last_index)

    def search_target(self, arr, target):
        mid = int(len(arr) / 2)
        if(arr[mid] == target):
            return mid
        elif(mid+1 < len(arr) and arr[mid] < target):
            return self.search_target(arr[mid+1:len(arr):1], target)
        elif(mid -1 > 0 and arr[mid] > target):
            return self.search_target(arr[0:mid-1:1], target)

# Fill this in.

# Test program
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
x = 2
obj = Solution(arr, x)
index = obj.search_target(arr, x)
print(obj.get_range(index))
# [1, 4]