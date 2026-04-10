class Solution:
	def maxProduct(self,arr):
		length=len(arr)
		pre_sum=1
		suf_sum=1
		temp=[arr[0],arr[length-1]]
		for i in range(length):
		    if arr[i]!=0:
		        pre_sum=pre_sum*arr[i]
		        temp.append(pre_sum)
		    if arr[length-i-1]!=0:
		        suf_sum=suf_sum*arr[length-i-1]
		        temp.append(suf_sum)
		    if arr[i]==0:
		        pre_sum=1
		    if arr[length-i-1]==0:
		        suf_sum=1
		    if arr[i]==0 and arr[length-i-1]==0:
		        temp.append(0)
		        
		        
		maximum=max(temp)
		return maximum
o1=Solution()
arr=[6,-3,-10,0,2]
ans=o1.maxProduct(arr)
