# Retruns the longest palindromic substring

class Solution:
    def longest_palindrome(self, s):
        palindrome_array = []
        for i in range(0, len(s)):
            for j in range(i+1, len(s)):
                sub = s[i: j]
                if(self.palindrome(sub)):
                    palindrome_array.append(sub)
        longest_palindrome = ""
        for l in range(1, len(palindrome_array)):
            if (len(palindrome_array[l]) > len(longest_palindrome)):
                longest_palindrome = palindrome_array[l]
        return longest_palindrome 

    def palindrome(self, s):
        palindrome = False
        half = int( len(s)/2)
        if (len(s)%2 == 0):
            if (s[0: half] == s[half: len(s)][::-1]):
                palindrome = True
        if (len(s)%2 == 1):
            if (s[0: half] == s[half+1: len(s)][::-1]):
                palindrome = True
        return palindrome


# Fill this in.

# Test program
s = "tracecars"
print(str(Solution().longest_palindrome(s)))
# racecar