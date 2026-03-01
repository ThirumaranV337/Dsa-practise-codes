class Solution:
    def maxWater(self, arr):
        length=len(arr)
        sum=0
        for i in range(length):#loop to point the current index value 
            max_1=arr[i]
            for j in range(0,i+1):#loop to find the left most longest building
                
                if arr[j]>max_1:
                    max_1=arr[j]
            max_2=arr[i]
            for k in range(i,length):#loop to find the right longest building
                
                if arr[k]>max_2:
                    max_2=arr[k]
            minimum=min(max_1,max_2)#find the minimum of both right and left 
            adder=minimum-arr[i]#to find the capacity
            if adder>=0:
                sum+=adder
        return sum    
arr=[3,0,2,0,4]
o1=Solution()
ans=o1.maxWater(arr)
print(ans)
'''
Time complexity in o(n^2)
Space complexity is o(n)
'''
