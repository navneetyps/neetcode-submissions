class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = len(numbers)
        l , r  = 0, l - 1
        while l < r:
            sum = numbers[l] + numbers[r]
            if sum == target:
                return [l+1,r+1]
            if sum > target:
                r -= 1
            if sum < target:
                l += 1
        
