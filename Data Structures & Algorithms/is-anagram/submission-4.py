class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        countS, countT ={},{}
        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i],0) + 1 ## get -> find this value in given position list if not found return 0
            countT[t[i]] = countT.get(t[i],0) + 1

        for k in countS:
            if countS[k] != countT.get(k,0): ## countS must have k but countT might not have -> use get
                return False
        
        return True