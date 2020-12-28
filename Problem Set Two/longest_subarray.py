# Returns the longest subarray

def longestSubarray(arr):
    # Write your code here
    new_arr = []
    array_list = [[]]
    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            if(arr[j] == arr[i] + 1):
                new_arr.append(arr[i])
        array_list.append(new_arr)
    longest = 0
    for l in range(0, len(array_list)):
        if(len(array_list[l]) > longest):
            longest = len(array_list[l])
    return longest


print(longestSubarray([5,1,2,3,4,5]))