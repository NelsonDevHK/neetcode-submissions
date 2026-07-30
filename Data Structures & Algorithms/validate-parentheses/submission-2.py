class Solution:
    def isValid(self, s: str) -> bool:
        map = {"[" : "]", "{": "}" , "(":")"}
        stack = []
        for c in s:
            if c in map:
                stack.append(c)
            elif c in map.values():
                if not stack or c != map[stack.pop()]:
                    return False
        return not stack
