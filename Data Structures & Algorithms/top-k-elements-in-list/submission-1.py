class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = Counter(nums)
        pq = []
        for key, val in mp.items():
            heapq.heappush(pq, (val,key))
            if len(pq) > k:
                heapq.heappop(pq)
        res = []
        while pq:
            res.append(heapq.heappop(pq)[1])
        return res