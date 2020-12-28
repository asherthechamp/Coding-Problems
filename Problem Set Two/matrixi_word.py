# Retruns if a matirx of characters reads a string in horizontal or vertical

def word_search(matrix, word):
    initial_row = len(matrix[0])
    initial_column = len(matrix)
    for i in range (0, initial_row):
        word_array = []
        for j in range (0, initial_column):
            word_array.append(matrix[j][i])
        matrix.append(word_array)
    if list(word) in matrix:
        return True
    else:
        return False

matrix = [
    ['F', 'A', 'C', 'I'],
    ['O', 'B', 'Q', 'P'],
    ['A', 'N', 'O', 'B'],
    ['M', 'A', 'S', 'S']]
print
print(word_search(matrix, 'ANOP'))
# True