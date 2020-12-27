# The maximum sum that can be found by adding a sub array of an array
def max_sub_array(arr):
    sub_arrays = []
    for i in range(0, len(arr)):
        sub_arrays += sub(arr[0: i+1])

    sum_sub_arr = []
    for arr in sub_arrays:
        sum_sub_arr.append (sum(arr))
    return max(sum_sub_arr)

# Constructs sub arrays
def sub(array):
    sub_arrays = [array]
    for i in range(1, len(array) - 1):
        sub_arrays.append(array[i:])
    return sub_arrays

print(max_sub_array([34, -50, 42, 14, -5, 86]))

