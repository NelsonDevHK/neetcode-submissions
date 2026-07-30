class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i , n in enumerate(nums):
            remain = target - n
            if remain in map:
                return [map[remain],i]
            map[n] = i
        return []