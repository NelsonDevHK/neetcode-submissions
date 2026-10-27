class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        for i in range(len(nums)):

            ##################  wrong approach  ##################            
            # we need to use (seen) cuz search in numset cause error of searching itself
            # numset = set(nums)
            # -(nums[i] + nums[j]) in numset:

            ##################  correct approach  ##################
            seen = set()
            for  j  in range(i+1,len(nums)):
                if -(nums[i] + nums[j]) in seen:
                    triplet = tuple(sorted((nums[i],nums[j],-(nums[i] + nums[j]))))
                    res.add(triplet)
                seen.add(nums[j])
        #res is map of tuple 
        #we want to return list of list. [ ] is the 1st | list(t) is 2nd.
        return [list(t) for t in res]
