class Solution:
    def rotateMatrix(self, mat):
        row=len(mat)
        for i in range(row):
            for j in range(i+1,row):
                mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
        return mat.reverse()
"""
1.Transpose the matrix
2.flip the matrix 
the main is without using the extra space
"""
