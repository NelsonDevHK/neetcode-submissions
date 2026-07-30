class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 !=  0:
            return False
        stack = []
        map = {"{":"}" ,"[":"]" ,"(":")"}
        for char in s:
            if char in map:
                stack.append(char)
            elif char in map.values():
                if not stack or char != map[stack.pop()]:
                    return False
        return not stack