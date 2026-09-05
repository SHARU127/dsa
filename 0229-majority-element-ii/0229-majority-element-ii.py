class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        hashmap = {}
        n = len(nums)
        condition = (n/3)
        extra = []
        for i in range(n):
            hashmap[nums[i]] = hashmap.get(nums[i],0)+1

        for key,value in hashmap.items():
            if value > condition:
                extra.append(key)

        return extra
         