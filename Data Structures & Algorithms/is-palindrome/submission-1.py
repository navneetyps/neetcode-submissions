class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        chars = []
        for c in s:
            #print(c)
            if (c >= 'a' and c <= 'z') or (c>='0' and c <= '9'):
                chars.append(c)
        st = ''.join(chars)
        l = len(st)
        i = 0
        j = l -1
        while(i <= j):
            if st[i] == st[j]:
                i+=1
                j-=1
            else:
                return False
        return True
            
        # print(st)
        # reversed_st = st[::-1]
        
        # #print(reversed_st)
        # if reversed_st == st:
        #     return True
        # return False
