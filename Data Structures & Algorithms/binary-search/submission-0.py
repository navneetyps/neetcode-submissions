class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mid = 0
        n = len(nums)
        l, h = 0,n-1
        while l <=h:
            mid = l + (int)((h-l)/2)
            can = nums[mid]
            if can == target:
                return mid
            elif can > target:
                h = mid - 1
            else:
                l = mid + 1
        return -1