class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        newslow = 0
        while True:
            slow = nums[slow]
            newslow = nums[newslow]
            if slow == newslow:
                return slow
        