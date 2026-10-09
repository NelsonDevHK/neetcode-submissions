class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}
        for word in strs:
            key = tuple(sorted(word))
            if key in hmap:
                hmap[key].append(word)
            else:
                hmap[key] = [word]
        return list(hmap.values())