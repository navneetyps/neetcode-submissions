class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for str in strs:
            s = ''.join(sorted(str))
            if s in dict:
                dict[s].append(str)
            else:
                dict[s] = [str]
        ans = [value for _,value in dict.items()]
        return ans