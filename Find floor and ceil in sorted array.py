class Solution:
    def findFloor(self, arr, x):
        length=len(arr)
        max=None
        index=None
        for i in range(length):
            if arr[i]==x:
                if not max:
                    max=arr[i]
                    index=i
                else:
                    if max<=arr[i]:
                        max=arr[i]
                        index=i
                
            elif arr[i]<=x:
                if not max:
                    max=arr[i]
                    index=i
                else:
                    if max<=arr[i]:
                        max=arr[i]
                        index=i
            elif arr[i]>x:
                if max==None:
                    return -1
                else:
                    return index
        return index
                    
o1=Solution()
arr=[1,2,8,10,10,12,19]   
x=11
ans=o1.findFloor(arr,x) 
