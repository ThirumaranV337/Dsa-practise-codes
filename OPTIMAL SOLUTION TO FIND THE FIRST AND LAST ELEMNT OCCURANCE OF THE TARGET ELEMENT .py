import bisect
class Solution:
    def find(self, arr, X):
        length=len(arr)
        left=bisect.bisect_left(arr,X)
        if arr[left]!=X:
            ans=[-1,-1]
            return ans
        elif arr[left]==X:
            right=bisect.bisect_right(arr,X)
            ans=[left,right-1]
            return ans
        
        
o1=Solution()
arr=[10 ,10, 12 ,13, 13, 16, 18 ,18 ,18 ,21]
x=10
ans=o1.find(arr,x)
###USING THE BINARY SEARCH LOWER BOUND AND UPPER BOUND TECHNIQUE
