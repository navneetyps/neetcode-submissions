class Solution:
    def canReach(self,nums,start,n):
        if start == n-1:
            return True
        elif start > n-1:
            return False
        if start in self.vis:
            return False
        for i in range (1,nums[start]+1):
            if start + i in self.vis:
                continue
            if self.canReach(nums,start+i,n):
                return True
        self.vis.add(start)
        return False


    def canJump(self, nums: List[int]) -> bool:
        self.vis = set()
        n = len(nums)
        return self.canReach(nums,0,n)
        
            