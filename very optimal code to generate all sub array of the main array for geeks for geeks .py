class Solution:
    def getSubArrays(self, arr):
        length=len(arr)
        returning_list=[]
        for i in range(length):
            appending_list=[]
            for j in range(i,length):
                if i==j:
                    element_appending=arr[i]
                    appending_list.append(element_appending)
                    returning_list.append(appending_list.copy())#here I use copy method becuse the appending in python perform only referance of the object  ,so I change it as a shallow  copy 
                else:
                    element_appending=arr[j]
                    appending_list.append(element_appending)
                    returning_list.append(appending_list.copy())
        return returning_list            
o1=Solution()
arr=[1,2,3]
ans=o1.getSubArrays(arr)
