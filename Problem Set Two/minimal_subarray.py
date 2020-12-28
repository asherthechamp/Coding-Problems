# Find the length of min subarray that would sum up to a target

def minSubArrayLen(nums, s):
    result_array = [0] * len(nums)
    for i in range(0, len(nums)):
        sum = 0
        j = i
        count = 0
        while(sum < s and j < len(nums)):
            sum += nums[j]
            j += 1
            count += 1
        if sum >= s:
            result_array[i] = count
        else:
            result_array[i] = len(nums)
    return min(result_array)



print(minSubArrayLen([2, 3, 1, 2, 3], 7))
