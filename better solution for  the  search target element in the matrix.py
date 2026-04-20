class Solution(object):
    def searchMatrix(self, matrix, target):
        m=len(matrix)
        n=len(matrix[0])
        if not matrix or not matrix[0]:
            return False
        for i in range(m):
                for j in range(n):
                  if matrix[i][j]==target:
                    return True
        return False
