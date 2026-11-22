class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        chars = []
        l = len(s)
        i = 0
        j = l -1
        while(i <= j):
            while(not s[i].isalnum() and i< l-1):
                i+=1
            while(not s[j].isalnum() and j> 0):
                j-=1
            if i > j:
                break
            if s[i] == s[j]:
                i+=1
                j-=1
            else:
                return False
        return True
