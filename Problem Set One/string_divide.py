# Checks if a string is divisible by a divisor substring

def string_divide(str1, str2):
    divisor = ""
    for i in range (1, len(str1)):
        if str1[i] == str1[0]:
            divisor = str1[0:i]
            break
    if str1.replace(divisor, "") == "" and str2.replace(divisor, "") == "":
        return divisor
    else:
        return ""

print(string_divide("ABABAB", "ABAB"))




