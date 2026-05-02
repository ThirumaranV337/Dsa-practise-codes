import math
class Solution:
	def nthRowOfPascalTriangle(self, n):
	    
	    row=n-1
        arr=[]
        for col in range(n):
            value=math.comb(row,col)
            arr.append(value)
        return arr
