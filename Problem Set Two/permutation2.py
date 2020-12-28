# Returns the permutations of a string

def permute(a, l, r, dict1):

    if l == r:
        print(a)
        dict1["".join(a)] = len(dict1) + 1
    else:
        for i in range(l, r + 1):
            a[l], a[i] = a[i], a[l]
            permute(a, l + 1, r, dict1)
            a[l], a[i] = a[i], a[l]

    return dict1

permute(["T", "U", "R", "I", "N", "G"], 0, 5, {})
print(permute(["T", "U", "R", "I", "N", "G"], 0, 5, {}))