# Reverses a string

def reverse_string(s):
    mid = len(s) // 2
    s = list(s)
    for i in range(0, mid):
        s[i], s[-1* (i + 1)] = s[-1*(i +1)], s[i]
    return s

print(reverse_string("love"))
