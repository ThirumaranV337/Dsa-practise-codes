class Solution(object):
    def findPeakGrid(self, mat):
        row=len(mat)
        col=len(mat[0])
        low=0
        high=col-1
        while low<=high:
            mid=(low+high)//2
            max=self.maximum_col(mat,mid)
            left_val=mat[max][mid-1] if mid > 0 else -1
            right_val=mat[max][mid+1] if mid < col-1 else -1
            if mat[max][mid]>left_val and mat[max][mid]>right_val:
                return [max,mid]
            elif left_val>mat[max][mid]:
                high=mid-1
            elif right_val>mat[max][mid]:
                low=mid+1
    def maximum_col(self,mat,col):
        max=mat[0][col]
        index=0
        column=len(mat)
        for i in range(column):
            if mat[i][col]>max:
                max=mat[i][col]
                index=i
        return index
            
