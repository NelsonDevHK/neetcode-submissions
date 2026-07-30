class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # if they are anagram
        # same no of Char same ASCII val
        res = defaultdict(list)  
        for s in strs:
            count = [0] *26
            for c in s:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)
        return list(res.values())