class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
        # charcounts = dict()
        # charcountt = dict()
        # for i in s:
        #     if i in charcounts:
        #         charcounts[i] = charcounts[i] + 1
        #     else:
        #         charcounts[i] = 1
        # for j in t:
        #     if j in charcountt:
        #         charcountt[j] = charcountt[j] + 1
        #     else:
        #         charcountt[j] = 1
        # if charcounts == charcountt:
        #     return True
        # else:
        #     return False

        