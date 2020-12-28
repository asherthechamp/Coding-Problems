# Returns the final state of the array if L pushes left and
# the domino falls left and R pushes right and the domino falls right
# And if the domino is pushed left and right it stays there

class Solution(object):
    def pushDominoes(self, dominoes):
        dominoes_array = list(dominoes)
        i = 0
        while i < len(dominoes):
            if dominoes[i] == "L" and i > 0:
                dominoes_array[i-1] = "L"
            if i < len(dominoes) -1 and dominoes_array[i] == "R" and dominoes_array[i+1] == ".":
                dominoes_array[i+1] = "R"
                i += 1
            if i < len(dominoes) -1 and dominoes[i] == "R" and dominoes[i+1] == "L":
                dominoes_array[i] = "."
                dominoes_array[i+1] = "."
                i += 1
            i += 1
        return "".join(dominoes_array)



print(Solution().pushDominoes('..R...L..R.'))
# ..RR.LL..RR