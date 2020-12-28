# Find the longest substring

class Solution:
    def length_of_longest_substring(self, s):
        count = 0
        counts_array = []
        for i in range(1, len(s)):
            if (s[i] == s[i-1]):
                counts_array.append(count+1)
                count = 0
            else:
                count += 1

        for i in range(1, len(counts_array)):
            if (counts_array [i] > counts_array [i-1]):
                largest_count = counts_array[i]
        return largest_count

print(str(Solution().length_of_longest_substring('abrkaabedefghijjxxx')))
