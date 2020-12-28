# Returns all possible tiles

def tiles_possibilities(s):
    count = 0
    freqDic = {}
    for c in s:
        if c in freqDic:
            freqDic[c] += 1
        else:
            freqDic[c] = 1
    factor = 1
    for val in freqDic.values():
        factor *= factorial(val)
    for i in range(1, len(s) + 1):
        count += factorial(len(s)) / (factorial(len(s)-i) * factor)
    return count

def factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

def permutation(s, count, dict1):

    if len(dict1) == factorial(len(s)):
        return dict1
    else:
        for i in range(0, len(s)):
            for j in range(0, len(s)):
                new_array = list(s)
                new_array[i], new_array[j] = new_array[j], new_array[i]
                new_string = "".join(new_array)
                count += 1
                if new_string not in dict1.keys():
                    dict1[new_string] = len(dict1) +1
                    permutation(new_string, count, dict1)

        return dict1

def part_perm(perm, s):
    count = 0
    for i in range (1, len(s) + 1):
        array =[]
        for p in perm:
            array.append("".join(list(p)[:i]))
        count += len(set(array))
    return count
#def all_permutations:

print (tiles_possibilities("AAABBC"))
print (part_perm(permutation("AAABBC", 0, {}), "AAABBC"))
