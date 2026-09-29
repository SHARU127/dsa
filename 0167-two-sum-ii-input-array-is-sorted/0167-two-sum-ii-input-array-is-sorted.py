class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        
        # for i in range(len(numbers)):
        #     for j in range(i+1,len(numbers)):
        #         if( numbers[i] + numbers[j] == target ):
        #             return [i+1,j+1]
        right =len(numbers)-1
        left=0
        while left < right:
            total = numbers[left] +numbers[right]
            if total == target:
                return [left+1 , right+1]
            elif total > target:
                right -=1
            else:
                left +=1
