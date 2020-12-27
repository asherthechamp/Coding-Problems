# Checks if a string can shift its last elemnet to first and become a second staring

def shiftable(A, B):
    no_of_shift = len(A) - 1
    i = 0
    test_str = A
    while i <= no_of_shift:
        new_sting = shift(test_str)
        if new_sting == B:
            return True
        else:
            test_str = new_sting
            i += 1
    return False

def shift(s):
    return s[1:] + s[:1]

print(shiftable('abcde', 'cedab'))
