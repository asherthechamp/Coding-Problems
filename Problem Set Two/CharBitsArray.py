# Checks if the end of bits array is a single bit or two bit
# 0 represents a single bit and 10 and 11 represents reperenst two bits
# And the array always ends with 0

def isOneBitCharacter(bits):
    i = 0
    while(i < len(bits)):
        if(bits[i] == 0):
            if(i == len(bits) - 1):
                i+=1
                return True
            else:
                i+=1
        else:
            if(i == len(bits) - 2):
                i+=1
                return False
            else:
                i+=2


print(str(isOneBitCharacter([0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0])))