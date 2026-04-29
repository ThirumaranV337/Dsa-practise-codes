import copy

class Solution(object):
    def setZeroes(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        
        # 1. Create a "snapshot" of how the matrix looks at the start
        duplicate = copy.deepcopy(matrix)
        for i in range(rows):
            for j in range(cols):
                if duplicate[i][j]==0:
                    for k in range(rows):
                        matrix[k][j]=0
                    for l in range(cols):
                        matrix[i][l]=0
        return matrix 
# Test
o1 = Solution()
matrix = [[9,-6,-1,-2,5],[-1,3,2147483647,-4,0],[-3,-4,0,4,-2147483648]]
ans = o1.setZeroes(matrix)
print(ans)
