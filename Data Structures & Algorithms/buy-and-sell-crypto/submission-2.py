class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = 101
        profit = 0
        for i in range(len(prices)):
            if i + 1  == len(prices):
                return profit
            if prices[ i ] < low:
                low = prices[i]
            if prices[ i + 1 ] - low > profit:
                profit = prices[ i + 1 ] - low
        return profit