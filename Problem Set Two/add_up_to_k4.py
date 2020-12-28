# Checks if sum of two elements in the array add up to k

def two_sum(arr, k):
    diffArray = []
    diffArray.append(k - arr[0])
    for i in range(1, len(arr)):
        if arr[i] in diffArray:
            return True
        else:
            diffArray.append(k-arr[i])
    return False

print(str(two_sum([4,7,0,-3,2], 5)))

def two_sum2(arr, k):
    for i in range(0, len(arr)):
        for j in range (i+1, len(arr)):
            if (arr[i] + arr[j] == k):
                return True
    return False

print(str(two_sum2([1, 1, 3, 4], 5)))