# Returns the permutaions of string

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

def factorial(n):
    factorial = 1
    for i in range(1, n+1):
        factorial *= i

    return factorial


print(permutation("TURING", 0, {}))