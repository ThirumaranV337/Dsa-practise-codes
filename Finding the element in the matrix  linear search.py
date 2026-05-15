class Solution:
    def searchMatrix(self, mat, x): 
    	row=len(mat)
    	col=len(mat[0])
    	for i in range(row):
    	    for j in range(col):
    	        if mat[i][j]==x:
    	            return True
    	return False
    	
    	
