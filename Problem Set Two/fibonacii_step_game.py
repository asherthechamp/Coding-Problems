# Number of ways you can jump a ladder given that you can make one or two jumps at time

def step_game(n):
    if (n > 2):
        step = [0] * n
    else:
        step = [0, 0]
    step[0] = 1
    step[1] = 2
    for i in range(2, n):
        step[i] = step[i-1] + step[i-2]
    return step[n-1]

print(step_game(4))
print(step_game(5))