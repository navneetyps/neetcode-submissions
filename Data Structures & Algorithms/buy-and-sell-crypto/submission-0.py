class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxi = 0
        for i in range(0,n):
            localmax = 0
            for j in range (i+1,n):
                localmax = max(localmax,prices[j]-prices[i])
            maxi = max(localmax,maxi)
        return maxi