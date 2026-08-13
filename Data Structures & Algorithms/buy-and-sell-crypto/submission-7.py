class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        entry = 101
        profit = 0
        for n in prices:
            entry = min(entry,n)
            profit = max(profit, n - entry)
        return profit