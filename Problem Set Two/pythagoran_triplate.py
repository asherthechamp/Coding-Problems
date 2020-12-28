# Checks if there is a pythagorian triplate

def findPythagoreanTriplets(nums):

    numsSquared = [0]*len(nums)
    sum_num_squared = 0
    for i in range(0, len(nums)):
        numsSquared[i] = nums[i] * nums[i]
        sum_num_squared += numsSquared

    for x in range(0, len(nums)):
        for y in range(x + 1, len(nums)):
            if nums[x] * nums [x] + nums[y] * nums[y] in numsSquared:
                return True

    return False
  # Fill this in.

print(str(findPythagoreanTriplets([3, 12, 5, 6])))
# True