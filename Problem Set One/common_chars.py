# Returns caharacters that are found in all words in an array

def common_chars(A):
    valid = True
    result = []
    for c in A[0]:
        for i in range(1, len(A)):
            if c in A[i]:
                A[0] = A[0].replace(c, "", 1)
                A[i] = A[i].replace(c, "", 1)
                valid = True
            else:
                valid = False
                break
        if valid:
            result.append(c)
            valid = True
    return result

print(common_chars(["cool","lock","cook"]))