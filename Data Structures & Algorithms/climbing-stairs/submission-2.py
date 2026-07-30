class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        prep,now = 1,2
        for i in range(3,n + 1):
            prep, now = now, prep + now
        return now
