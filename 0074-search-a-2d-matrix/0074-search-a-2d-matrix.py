class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        top =0 
        bot = len(matrix)-1

        while top <= bot:
            mid = (top+bot)//2           #changed the code from matrix[mid][bot]
            if matrix[mid][0] < target and matrix[mid][-1] > target:
                break

            elif matrix[mid][0] > target:
                bot = mid -1

            else:
                top = mid +1
        
        row = (top+bot)//2
        left =0
        right = len(matrix[row])-1

        while left <= right:
            mid =(left+right)//2
            #at first i had written it in matrix[right][mid]
            if matrix[row][mid] == target:
                return True
            if matrix[row][mid] > target:
                right = mid -1
            else:
                left = mid +1
        return False

