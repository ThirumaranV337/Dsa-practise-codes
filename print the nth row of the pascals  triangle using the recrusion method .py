import math
class Solution:
	def nthRowOfPascalTriangle(self, n):
	   return self.recursion_to_row(n-1,0,[])
	def recursion_to_row(self,row,col,arr):
	    if col>row:
	        return arr
	    value=math.comb(row,col)
	    arr.append(value)
	    return self.recursion_to_row(row,col+1,arr)
	
