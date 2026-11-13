class Solution:
    def maxSubarraySum(self, arr, k):
        # code here 
      
        curr_window=0
        for i in range(k):
            curr_window+=arr[i]
        max_sum=curr_window 
        for j in range(k,len(arr)):
            curr_window+=arr[j]
            curr_window-=arr[j-k]
            if curr_window>max_sum:
                max_sum=curr_window
          
        return max_sum    
            
            
            

o1=Solution()
ans=o1.maxSubarraySum([100, 200, 300, 400],2)
