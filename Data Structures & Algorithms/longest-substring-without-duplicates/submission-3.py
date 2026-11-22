class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0 or n == 1:
            return n
        longest_substring_length, local_longest = 1,1
        unique = dict()
        unique[s[0]] = 0
        start = 0
        for i in range(1,n):
            if s[i] in unique and unique[s[i]] >= start:
                index = unique[s[i]]
                longest_substring_length = max(local_longest,longest_substring_length)
                start = index + 1
                local_longest = min(local_longest,i - start + 1)
            else:
                local_longest+=1
            unique[s[i]] = i
        return max(local_longest,longest_substring_length)

