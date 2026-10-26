class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0

        for n in numset:
        # we only start at the smallest element exist in set (n - 1) DNE
            if (n - 1) not in numset:
                length  = 1 #this is count on every starting exist in set
                while (n + length) in numset:
                    length += 1
                longest = max (length, longest)
        return longest