class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        unique = {}
        longest = 0

        for i in range(len(s)):
            if s[i] in unique and unique[s[i]] >= start:
                start = unique[s[i]] + 1

            unique[s[i]] = i
            longest = max(longest, i - start + 1)

        return longest