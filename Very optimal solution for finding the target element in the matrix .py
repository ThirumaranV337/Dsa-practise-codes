class Solution(object):
    def searchMatrix(self, matrix, target):
        m=len(matrix)
        n=len(matrix[0])
        left=0 
        right=m*n-1
        while left<=right:
            mid=(left+right)//2
            row=mid//n
            column=mid%n
            if matrix[row][column]==target:
                return True
            elif matrix[row][column]<target:
                left=mid+1
            elif matrix[row][column]>target:
                right=mid-1
        return False
            
