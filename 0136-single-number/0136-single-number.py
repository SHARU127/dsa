class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n= len(nums)
        single_no=0
        for x in nums:
            single_no ^= x
        return single_no