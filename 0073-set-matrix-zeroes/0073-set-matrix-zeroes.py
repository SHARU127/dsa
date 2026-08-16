class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        m,n = len(matrix), len(matrix[0])
        rowZero = False


#now we need to check every index, and mark the first row 0 or first column as 0
        for r in range(m):
            for c in range(n):

                if matrix[r][c] == 0:
                    matrix[0][c] = 0

                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True


        #now we set the values as zero for the row which is zero or the coloumn is 0
        for r in range(1,m):
            for c in range(1,n):
                if matrix[0][c] ==0 or matrix[r][0]==0:
                    matrix[r][c] =0

        
        #now the first row with 0, will get whole first coloumn as 0
        if matrix[0][0] == 0:
            for r in range(m):
                matrix[r][0] = 0

        if rowZero:
            for c in range(n):
                matrix[0][c] = 0

        

        