class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ""
        for c in s:
            if c.isalnum():
                word += c.lower()
        print(word)
        return word == word[::-1]