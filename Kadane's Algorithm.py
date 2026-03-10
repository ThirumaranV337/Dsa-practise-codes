class Solution:
    def maxSubarraySum(self, arr):
        maximum_sum_value=None
        length_arr=len(arr)
        sum_value=0
        for i in range(length_arr):
            sum_value+=arr[i]
            
            if maximum_sum_value==None:
                maximum_sum_value=sum_value
            
            if sum_value>maximum_sum_value:
                maximum_sum_value=sum_value
            if sum_value<0:
                sum_value=0
           
        return maximum_sum_value
o1=Solution()
arr=[2,3,-8,7,-1,2,3]
ans=o1.maxSubarraySum(arr)
                
        
                    
                
                
            
        
