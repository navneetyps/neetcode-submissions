class Solution:
    def findPalindrome(self,s:str,l:int,r:int,local_longest:int,n:int)->None:
        while l >= 0 and r<n and s[l] == s[r]:
                local_longest +=2
                if local_longest> self.longest:
                    self.longest = local_longest
                    self.ans = s[l:r+1]
                l-=1
                r+=1
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        self.longest = 1
        self.ans = s[0]
        for i in range(n):
            #odd
            local_longest = 1
            l,r = i-1, i+1
            self.findPalindrome(s,l,r,local_longest,n)
            #even
            local_longest = 0
            l,r = i, i+1
            self.findPalindrome(s,l,r,local_longest,n)
        return self.ans
