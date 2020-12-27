# Finds the smallest number that can be made by removing k digits from a number

def smallest_number(num, k):
    result = ""
    len_new_num = len(num) - k
    for i in range(0, len_new_num):
        end_index = len(num) - (len_new_num - i) + 1
        sub = num[: end_index]
        if result == "" and "0" in sub:
            sub_s = sub.replace("0", "")
        else:
            sub_s = sub
        new_index = num.index(min(sub_s))
        result += num[new_index]
        num = num[new_index + 1:]
    return result

print (smallest_number("14032219", 3))
