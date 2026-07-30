class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = {}
        for i , n in enumerate(nums):
            if n in map:
                return True
            map[n] = i
        return False 