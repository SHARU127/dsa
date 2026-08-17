class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        index =-1
        #why -2, cuz the next permutation u get at break point, the break point would be after the first element,
        for i in range(len(nums)-2,-1,-1):
            if nums[i] < nums[i+1]:
                index = i
                break

        #if we dont get a break point then it means that, the array is decs order, return the first element in permutation
        if index == -1:
            nums.reverse()
            return


        #now after finding the index(breakpoint), swap with smallest number greater than index
        for i in range(len(nums)-1,index,-1):
            if nums[index] < nums[i]:
                nums[index],nums[i] = nums[i],nums[index]
                break
        nums[index+1:] = reversed(nums[index+1:]) 



