class Solution:
    def reverseBits(self, n: int) -> int:
        pwr = 31
        res = 0
        for i in range(32):
            if n % 2 == 1:
                res += pow(2,pwr)
            pwr -= 1
            n = n >> 1
        return res