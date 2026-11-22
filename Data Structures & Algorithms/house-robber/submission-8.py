class Solution:
    # Recursive solution
    def maxAmount(self,nums,houses,index):
        if index >= houses:
            return 0
        return max(nums[index] +self.maxAmount(nums,houses,index+2),self.maxAmount(nums,houses,index+1))

    def rob(self, nums: List[int]) -> int:
        houses = len(nums)
        if houses == 0:
            return 0
        if houses<= 2:
            return max(nums)
        # recursive solution
        # return max(self.maxAmount(nums,houses,0),self.maxAmount(nums,houses,1))

        # dp solution
        # dp = [0] * (houses + 1)
        # dp[0] = nums[0]
        # dp[1] = max(nums[0],nums[1])
        # for i in range(2,houses):
        #     dp[i] = max(nums[i]+ dp[i-2],dp[i-1])
        # return dp[houses-1] 

        #dp solution space optimized
        rob1, rob2 = nums[0],max(nums[0],nums[1])
        for i in range(2,houses):
            newRob = max(nums[i]+rob1,rob2)
            rob1 = rob2
            rob2 = newRob
        return newRob

