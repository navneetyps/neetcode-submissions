class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans_dict = set()
        nums = sorted(nums)
        n = len(nums)
        for i in range(n-1):
            diff = nums[i];
            j = i + 1
            k = n - 1
            while j < k:
                sum = nums[j] + nums[k]
                if sum + diff == 0:
                    ans_dict.add((nums[i],nums[j],nums[k]))
                    k -= 1
                    j += 1
                elif sum + diff > 0:
                    k -= 1
                else:
                    j += 1
        return list(ans_dict)