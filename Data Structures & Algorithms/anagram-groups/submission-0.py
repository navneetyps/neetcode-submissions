class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        list = [0] * 26
        dict = {}
        ans = []
        n = len(strs)
        for str in strs:
            list = [0] * 26
            for s in str:
                list[ord(s)- ord('a')] += 1
            key = tuple(list)
            if key not in dict:
                dict[key]=[str]
            else: dict[key].append(str)
        for value in dict.values():
            ans.append(value)
        return ans
        