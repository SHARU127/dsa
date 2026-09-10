class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        
        abvrow = [1]*n

        for _ in range(m-1):
            currow = [1]*n
            for i in range(1,n):
                currow[i] = currow[i-1]+abvrow[i]
            abvrow = currow
        return abvrow[-1]
                
                