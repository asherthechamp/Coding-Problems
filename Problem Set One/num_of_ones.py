# Returns the humming weight of a number

def hammingWeight(n: int) -> int:

    return bin(n)[2:].count("1")
print(hammingWeight(11))

# 00000000000000000000000000001011