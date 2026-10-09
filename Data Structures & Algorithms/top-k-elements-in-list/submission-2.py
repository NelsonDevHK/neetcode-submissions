class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        res = []
        top = 0
        for n in nums:
            if n in hmap:
                hmap[n] += 1
            else:
                hmap[n] = 1
        while k > 0:
            print(max(hmap,key = hmap.get))
            kTop = max(hmap,key = hmap.get)
            res.append(kTop)
            del hmap[kTop]
            k -= 1
        return res