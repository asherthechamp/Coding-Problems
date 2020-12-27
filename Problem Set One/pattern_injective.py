# Checks if string follows a pattern

def pattern_injective(pattern, s):
    pattern_dict = {}
    words = s.split(" ")
    for i, c in enumerate(pattern):
        if len(pattern) != len(words):
            return False
        elif pattern_dict != {} and c in pattern_dict.keys():
            if pattern_dict[c] == words[i]:
                continue
            else:
                return False
        elif words[i] not in pattern_dict.values():
            pattern_dict[c] = words[i]
        else:
            return False
    return True

print(pattern_injective("aa", "aa aa aa aa"))