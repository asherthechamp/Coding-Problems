# Returns the numeber of parethesis that can be formed from a sting of opening and closing parenthesis

def prem_paretnthesis(s):
    opening = 0
    closing = 0
    result = ""
    sub = ""
    count = 0
    for c in s:
        sub += c
        if c == "(":
            opening += 1
            count += 1
        if c == ")":
            closing += 1
            count += 1
        if opening == closing:
            result += sub[1:count-1]
            sub = ""
            count = 0
    return result

print(prem_paretnthesis("()()"))
# "(()())(())(()(()))"