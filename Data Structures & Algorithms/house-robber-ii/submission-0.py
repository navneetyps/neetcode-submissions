class Solution:
    def robMax(self,nums,start,end):
        if end - start == 1:
            return nums[start]
        rob1, rob2 = nums[start],max(nums[start],nums[start+1])
        print (rob1,rob2)
        newRob = 0
        for i in range(start+2,end):
            newRob = max(nums[i]+rob1,rob2)
            rob1 = rob2
            rob2 = newRob
        return rob2
    def rob(self, nums: List[int]) -> int:
        houses = len(nums)
        if houses == 0:
            return 0
        if houses<= 2:
            return max(nums)
        return max(self.robMax(nums,0,houses-1),self.robMax(nums,1,houses))


 