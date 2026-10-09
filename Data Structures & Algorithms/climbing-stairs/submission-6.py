class Solution:
    def climbStairs(self, n: int) -> int:
        # base case
        if n <= 2:
            return n
        #after line 5, n must be greater than 3
        prev , now = 1,2 
        for i in range(3,n + 1): # n + 1 stops at n
            prev, now = now , prev + now
        return now
