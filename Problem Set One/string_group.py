# Groups strings in a length of four

def string_group(S, K):
    index = S.index("-")
    first_str = ""
    if index > K:
        first_str = S[0:K].upper()
        index = K
    else:
        first_str = S[0:index]
    result_str = [first_str]
    rest_str = S[index:]
    rest_str = rest_str.replace("-", "")
    i = 0
    j = 4
    while j <= len(rest_str):
        sub = rest_str[i:j].upper()
        result_str.append(sub)
        i = j
        if j + 4 <= len(rest_str):
            j += 4
        elif j == len(rest_str):
            break
        else:
            j = len(rest_str)
    answer = "-".join(result_str)
    return answer

print(string_group("5F3Z-2e-9-w", 4))

