class Solution:
    def longestSubarray(self, arr, k):  
        length=len(arr)
        max_length=0
        for i in range(length):
            sum=0 
            for j in range(i,length):
                sum+=arr[j]
                if sum==k:
                    new_length=j-i+1
                    max_length=max(max_length,new_length)
                    #do not use break kere because it will not give accurate answer
       return max_length   
o1=Solution() 
arr=[10,5,2,7,1,-10]
k=15
ans=o1.longestSubarray(arr,k)
#time complexity o(n^2)
              
