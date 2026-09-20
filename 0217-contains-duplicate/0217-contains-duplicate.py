from collections import defaultdict 
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        
        hashmap = defaultdict(int)

        for ch in nums:
            hashmap[ch] += 1

        for key,value in hashmap.items():
            if value >= 2:
                return True

        return False



