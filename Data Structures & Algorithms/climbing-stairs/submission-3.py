class Solution:
    def climbStairs(self, n: int) -> int:
        #base case would be 0,1,2
        if n <= 2:
            return n
        #reach here n must be 3+
        prev, now = 1,2
        for n in range(3, n + 1):
           prev , now = now , now + prev
        return now