class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprof = 0
        minprice = prices[0]
        for pr in prices:
            maxprof = max(maxprof, pr - minprice)
            minprice = min(pr, minprice)
        return maxprof
        