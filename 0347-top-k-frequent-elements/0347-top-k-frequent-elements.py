from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hashh = defaultdict(int)
        res = []
        for i in range(len(nums)):
            hashh[nums[i]] +=1
        
        
        # for key,value in hashh.items():
        #     if value > k:
        #         res.append(key)

        # return res
        n=k
        while n >0:
            

            mx = max(hashh, key=hashh.get)
            res.append(mx)
            hashh.pop(mx)
            n-=1

        return res