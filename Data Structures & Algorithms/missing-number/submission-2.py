class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        size = len(nums)
        mp = [None] * (size + 1)

        for x in nums:
            mp[x] = 1             
        return mp.index(None) 
