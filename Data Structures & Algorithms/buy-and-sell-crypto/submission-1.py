class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        maxi,maxsofar = 0,0
        while l<r and r< len(prices):
            if prices[l] <= prices[r]:
                maxsofar = max(maxsofar,prices[r]-prices[l])
                maxi = max(maxi,maxsofar)
            else:
                l = r
            r+=1
        return maxi