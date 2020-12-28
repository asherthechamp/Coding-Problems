# Python3 program to find the number of ways to get sum 'x' with 'n' dice
# where every dice has 'm' faces

# The main function that returns number of ways to get sum 'x'
# with 'n' dice and 'm' with m faces.
def findWays(m, n, x):
    modulo = 10 ** 9 + 7
    # Create a table to store results of subproblems. One extra
    # row and column are used for simpilicity (Number of dice
    # is directly used as row index and sum is directly used
    # as column index). The entries in 0th row and 0th column
    # are never used.
    table = [[0] * (x + 1) for i in range(n + 1)]  # Initialize all entries as 0

    for j in range(1, min(m + 1, x + 1)):  # Table entries for only one dice
        table[1][j] = 1

    # Fill rest of the entries in table using recursive relation
    # i: number of dice, j: sum
    for i in range(2, n + 1):
        for j in range(1, x + 1):
            for k in range(1, min(m + 1, j)):
                table[i][j] += table[i - 1][j - k]

    # Uncomment above line to see content of table

    return table[-1][-1] % modulo



def numRollsToTarget( d: int, f: int, target: int):
    modulo = 10 ** 9 + 7
    cache = {}

    def numRollsToTargetHelper(dd, tt):
        if cache.get((dd, tt)) != None:
            return cache[(dd, tt)]
        nonlocal f
        if dd == 1:
            if tt <= f:
                return 1
            else:
                return 0

        ret = 0
        for i in range(1, f + 1):
            if tt - i > 0:
                ret += numRollsToTargetHelper(dd - 1, tt - i)
        cache[(dd, tt)] = ret
        return ret

    ret = numRollsToTargetHelper(d, target)
    return ret % modulo
print(findWays(30, 30 , 500))
print(numRollsToTarget(30, 30, 500))