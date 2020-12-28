# Retrun the most common word which is not in the banned words list

def mostCommonWord(paragraph: str, banned: list[str]) -> str:
    paragraph = paragraph.lower()

    paragraph = re.sub(r'[^\w\s]*', '', paragraph)
    paragraphArray = paragraph.split(" ")
    array = list(set(paragraphArray))
    freqDic = dict.fromkeys(set(paragraphArray), 0)

    for i in range(0, len(paragraphArray)):
        if (paragraphArray[i] in freqDic.keys()):
            freqDic[paragraphArray[i]] += 1
        else:
            freqDic[paragraphArray[i]] = 1
    sorted_tuples = sorted(freqDic.items(), key = lambda x: (x[1]))

    for i in range(-1, -1 * len(sorted_tuples), -1):
        if(not (sorted_tuples[i][0] in banned)):
            return sorted_tuples[i][0]


paragraph1 = "Bob hit a ball, the hit BALL flew far after it was hit. ball ball  bag bag"
banned1 = ["hit", "ball"]

print(mostCommonWord(paragraph1, banned1))