class Solution:
    def maxArea(self, height: list[int]) -> int:
        left =0
        right=len(height)-1
        max_ar=0
        while left < right:
            max_ar = max(max_ar, (right-left)* min(height[left],height[right]))
            if height[left] < height[right]:
                left +=1
            else:
                right -=1
        return max_ar
            
