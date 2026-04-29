# Your task is to complete this function
import copy

class Solution(object):
    def setZeroes(self, matrix):
        row=len(matrix)
        column=len(matrix[0])
        duplicate=copy.deepcopy(matrix)
        for i in range(row):
            for j in range(column):
                if matrix[i][j]==0:
                    ##here we are going to column wise all element ,the row shuuld be fixed 
                    for k in range(column):
                        if matrix[i][j]==-1:
                            matrix[i][j]=0
                        elif matrix[i][k]!=0:
                            matrix[i][k]=-1
                    ##here we are going  to row wise all element ,the coulmn should to fixed
                    for l in range(row):
                        if matrix[l][j]==-1:
                            matrix[l][j]=0
                        elif matrix[l][j]!=0:
                            matrix[l][j]=-1
                        
        for m in range(row):
            for z in range(column):
                if matrix[m][z]==-1 and duplicate[m][z]!=-1:
                    matrix[m][z]=0
        return matrix
o1=Solution()
matrix=[[9,-6,-1,-2,5],[-1,3,2147483647,-4,0],[-3,-4,0,4,-2147483648]]
ans=o1.setZeroes(matrix)
ans=o1.setZeroes(matrix)
