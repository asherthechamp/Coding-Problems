# Checks if all characters exist in one subsring
# and not the other and returns the substrings

def one_sub_string(S):
    result = []
    # creates a substring
    sub_s = []
    # Keeps track of the distinct characters in substring
    dis_ss = []
    while(S):
        sub_s.append(S[0])
        if S[0] != dis_ss:
            dis_ss.append(S[0])
        S= S[1:]
        # Checks if the sub_string ended and no char exists in the remaining sub string
        done_with_ss = True
        for c in dis_ss:
            if c in S:
                done_with_ss = False
                break
        if done_with_ss:
            result.append(sub_s)
            sub_s = []
            dis_ss = []
        else:
            continue
    return result

print(one_sub_string("ababcbacadefegdehijhklij"))


