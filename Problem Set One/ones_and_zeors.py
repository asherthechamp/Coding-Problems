def ones_and_zeros(s):
    i = 0
    diff = len(s) - i
    while diff > 2:
        if s[i] == 0:
            i += 1
        if s[i] == 1:
            i += 2
        diff = len(s) - i
    if (diff == 2 or diff == 1) and s[i] == 0:
        return True
    else:
        return False

print(ones_and_zeros([1, 1, 1, 0]))

