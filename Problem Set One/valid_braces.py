# Retruns the valid strings given the number of paris of opening and closing parenthesis

def valid_braces(n):
    results = ["("]
    for j in range(2, 2 * n + 1):
        results = advance(results, n)
    return results

def advance(results, n):
    new_array = []
    for result in results:
        if result:
            if add_parenthesis("(", result, n):
                string1 = add_parenthesis("(", result, n)
                new_array.append(string1)
            if add_parenthesis(")", result, n):
                string1 = add_parenthesis(")", result, n)
                new_array.append(string1)
    return new_array

def add_parenthesis(c, s, n):
    if s and c == ("(") and len(s) < 2*n - 1 and s.count("(") < n:
        return s + c
    if s and c == (")") and s.count("(") > s.count(")"):
        return s + c

print(valid_braces(3))



