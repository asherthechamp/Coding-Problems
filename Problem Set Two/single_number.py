# Returns array of numbers that are not repeated

def single_number(nums):
    copy_array = []
    copy_array.append(nums[0])
    for i in range (1, len(nums)):
        if nums[i] in copy_array:
            copy_array.remove(nums[i])
        else:
            copy_array.append(nums[i])
    return copy_array[0]


print (str(single_number([4, 3, 2, 4, 1, 1, 5, 3, 2] )))
# 1