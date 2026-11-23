class Solution:
    def findPalindrome(self,s:str,l:int,r:int)->None:
        n = len(s)
        while l >= 0 and r<n and s[l] == s[r]:
                l-=1
                r+=1
        return s[l+1:r]

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans = s[0]
        for i in range(n):
            #odd
            odd = self.findPalindrome(s,i,i)
            #even
            even = self.findPalindrome(s,i,i+1)
            if len(odd) > len(ans):
                ans = odd
            if len(even) > len(ans):
                ans = even   
        return ans
