# Returns the latest time that can be formed for array of numbers

def latest_time(arr):
    time_string_arr = []
    for i in range (0, len(arr)):
        if arr[i] in [0, 1, 2]:
            for j in range(0, len(arr)):
                if j != i:
                    for x in range(0, len(arr)):
                        if x != i and x != j:
                            if arr[x] in [0, 1, 2, 3, 4, 5]:
                                for y in range(0, len(arr)):
                                    if y != i and y != j and y != x:
                                        if arr[i] == 2:
                                            if arr[j] in [0, 1, 2, 3]:
                                                time_string = str(arr[i])+str(arr[j]) + ":" + str(arr[x]) + str(arr[y])
                                                time_string_arr.append(time_string)
                                        else:
                                            time_string = str(arr[i])+str(arr[j]) + ":" + str(arr[x]) + str(arr[y])
                                            time_string_arr.append(time_string)
    return max(time_string_arr)

print(latest_time([1,2,3,4]))

