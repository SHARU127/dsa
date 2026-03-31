class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        key =0
        for i in range(n):
            key = nums[i]
            j= i-1
    
    #shift ele that are greater than key 
            while j >= 0 and nums[j] > key:
                nums[j+1] = nums[j]
                j -= 1
            nums[j+1] = key

        print(nums) 



        