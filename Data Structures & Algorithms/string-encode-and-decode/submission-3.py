class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "EMPTY_LIST"
        res =""
        return "SPLITTER".join(strs)
    def decode(self, s: str) -> List[str]:
        res = []
        if s == "EMPTY_LIST":
            return []
        return s.split("SPLITTER")