class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprof = 0
        minprice = prices[0]
        for pr in prices:
            profit = pr - minprice
            maxprof = max(maxprof, profit)
            minprice = min(pr, minprice)
        return maxprof
        