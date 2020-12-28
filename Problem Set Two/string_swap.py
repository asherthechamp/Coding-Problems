class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        answer = False
        if (A == B and A != B[::-1]):
            return False
        else:
            for i in range(0, len(A)):
                if (A[i] in B ):
                    return True
                else:
                    return False
        return answer

print(Solution().buddyStrings("ab", "ab"))
