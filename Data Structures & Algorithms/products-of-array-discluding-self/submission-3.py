class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res= [1] * len(nums)
        prefix , postfix = 1,1

        for i in range(len(nums)):
            res[i] = prefix
            prefix = prefix * nums[i]
        
        for i in range(len(nums) -1, -1 ,-1): # Started at nums[last element]
        #since we use res as the return to save space
            res[i] = res[i] * postfix #starting at last element to product asked is equal to prefix cuz postfix = 0
            postfix = postfix * nums[i]

        return res
