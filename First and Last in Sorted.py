class Solution:
    def find(self, arr, x):
        length=len(arr)
        first=-1
        last=-1
        for i in range(length):
            if arr[i]==x:
                if first==-1:
                    first=i
                
                last=i
        temp=[first,last]
        return temp
o1=Solution()
arr=[10 ,10, 12 ,13, 13, 16, 18 ,18 ,18 ,21]
x=10
ans=o1.find(arr,x)
