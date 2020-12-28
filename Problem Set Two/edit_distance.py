# The edit distance it takes to make change to a string and turn it to another

def calculate_edit_distance(s1, s2):
    longer_string = ""
    shorter_string = ""
    if len(s1) >= len(s2):
        longer_string = s1
        shorter_string = s2
    else:
        longer_string = s2
        shorter_string = s1
    str_array = list(longer_string)
    for i in range(0, len(shorter_string)):
        if shorter_string[i] in longer_string:
            str_array.remove(shorter_string[i])
    return len(str_array)

print (calculate_edit_distance('biting', 'sitting'))
# 2
