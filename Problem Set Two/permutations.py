# Returns the number of tile possibilites

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        length = len(tiles)
        freq = []
        unqstr = list(set(list(tiles)))
        copyTiles= list(tiles).copy()

        # finding frequency of all the lower
        # case alphabet and storing them in
        # array of integer
        for i in range(0, len(unqstr)):
            occ = 0
            while (unqstr[i] in list(copyTiles)):
                copyTiles.remove(unqstr[i])
                occ += 1
            freq.append(occ)

                # finding factorial of number of
        # appearances and multiplying them
        # since they are repeating alphabets
        fact = 1
        for i in range(0, len(freq)):
            fact = fact * self.factorial(freq[i])

            # finding factorial of size of string
        # and dividing it by factorial found
        # after multiplying
        return self.factorial(length) / fact

    def factorial(self, n):
        if (n == 1):
            return 1
        else:
            return n * self.factorial(n-1)

print(str(Solution().numTilePossibilities("AAABBC")))