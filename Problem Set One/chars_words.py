# Checks if all characters of words are found in a character array

def chars_words(words, chars):
    valid_words = []
    for word in words:
        for char in word:
            if char in chars:
                valid = True
            else:
                valid = False
                break
        if valid:
            valid_words.append(word)
    result_str = "".join(valid_words)
    return len(result_str)

print(chars_words(["hello","world","leetcode"], "welldonehoneyr"))

