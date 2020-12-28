def num_ways(n, m):
    return traverse((0, 0), (m, n))
def m_move(i, j):
    return (i, j+1)
def n_move(i, j):
    return (i+1, j)
def check(a, b):
    return a == b
def traverse(x, y):
    if check(n_move(x[0], x[1]), (y[0], y[1])):
        return 1
    else:
        return 0 + traverse(n_move(x[0], x[1]), (y[0], y[1]))
    if check(m_move(x[0], x[1]), (y[0], y[1])):
        return 1
    else:
        return 0 + traverse(m_move(x[0], x[1]), (y[0], y[1]))
    return 0


def numberOfPaths(m, n):
    if (m == 1 or n == 1):
        return 1
    return numberOfPaths(m - 1, n) + numberOfPaths(m, n - 1)


# Driver program to test above function
m = 2
n = 2
print(numberOfPaths(m, n))


# print(num_ways(2, 2))
# 2 