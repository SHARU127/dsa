from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashh = defaultdict(int)
        if len(s) != len(t):
            return False
            
        for ch in s:
            hashh[ch] +=1
        for x in t:
            if x not in hashh or hashh[x] == 0:
                return False
            hashh[x] -= 1

        return True 