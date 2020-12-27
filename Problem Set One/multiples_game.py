# Players take turn and show select a factor of a n, after each move selecting x
# the n becomes n - x and if only the first player wins

def multiples_game(N):
    x = 1
    factors = find_factors(N)
    for i in range(0, len(factors)):
        count = 0
        factors2 = factors
        j = 0
        while N != 1:
            for l in range(0, len(factors2)):
                count += 1
                N = N - factors2[l]
            factors2 = find_factors(N - factors[i])
        if count % 2 == 0:
            return False
    return True

def find_factors(n):
    if n == 1:
        return [1]
    x= 1
    factors = []
    while x <= n/2:
        if n%x == 0:
            factors.append(x)
        x += 1
    return factors

print(multiples_game(3))
