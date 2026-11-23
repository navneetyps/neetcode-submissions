class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        longest = 1
        ans = s[0]
        for i in range(n):
            #odd
            local_longest = 1
            l,r = i-1, i+1
            while l >= 0 and r<n and s[l] == s[r]:
                local_longest +=2
                if local_longest> longest:
                    longest = local_longest
                    ans = s[l:r+1]
                l-=1
                r+=1
            #even
            local_longest = 0
            l,r = i, i+1
            while l >= 0 and r<n and s[l] == s[r]:
                local_longest +=2
                if local_longest> longest:
                    longest = local_longest
                    ans = s[l:r+1]
                l-=1
                r+=1
        return ans
