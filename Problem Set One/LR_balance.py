# Balances the number of L and R in a substring

def lr_balance(s):
    result = []
    sub = s[0]
    for i in range (1, len(s)):
        sub += s[i]
        if sub.count("L") == sub.count("R"):
            result.append(sub)
            sub = ""
        else:
            continue
    return result

print(lr_balance("RLLLLRRRLR"))

