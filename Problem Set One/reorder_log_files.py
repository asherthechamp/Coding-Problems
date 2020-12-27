# Reorders log files

def reoder_log_files(logs):
    alpha_dict = {}
    num_dict = {}
    for i in range(0, len(logs)):
        words = logs[i].split(" ")
        id = words[0]
        log = " ".join(words[1:len(words)])
        if not log[0].isnumeric():
            alpha_dict[id] = log
        else:
            num_dict[id] = log
    sorted_alpha_dict = sorted(alpha_dict.items(), key=lambda x: (x[1], x[0]))
    result = []
    for i in range(0, len(sorted_alpha_dict)):
        result.append(sorted_alpha_dict[i][0] + " " + sorted_alpha_dict[i][1])
    num_dict_array = list(num_dict.items())
    for i in range(0, len(num_dict_array)):
        result.append(num_dict_array[i][0] + " " + num_dict_array[i][1])

    return result

print(reoder_log_files(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))