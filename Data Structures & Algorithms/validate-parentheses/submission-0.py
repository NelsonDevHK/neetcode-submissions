class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')': '(', ']': '[', '}': '{'}
        stack = []
        for ch in s:
            if ch in "([{": stack.append(ch)
            elif stack and pairs.get(ch) == stack[-1]: stack.pop()
            else: return False
        return not stack    