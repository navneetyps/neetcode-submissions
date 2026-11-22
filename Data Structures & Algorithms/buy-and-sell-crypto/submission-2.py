class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy,sell = 0,1
        maximum,maxsofar = 0,0
        while buy<sell and sell< len(prices):
            if prices[buy] <= prices[sell]:
                maxsofar = max(maxsofar,prices[sell]-prices[buy])
                maximum = max(maximum,maxsofar)
            else:
                buy = sell
            sell+=1
        return maximum