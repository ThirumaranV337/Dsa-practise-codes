class Solution:
    def firstNegInt(self, arr, k): 
        initial_window=[]
        ans=[]
        for i in range(k):
            if arr[i]<0:
                initial_window.append(arr[i])
        if len(initial_window)!=0:
            ans.append(initial_window[0])
        else:
            ans.append(0)
            
        for j in range(k,len(arr)):
            if len(initial_window)!=0:
                if  initial_window[0]==arr[j-k]:
                    initial_window.pop(0)
            if arr[j]<0:
                initial_window.append(arr[j])
            if len(initial_window)==0:
                ans.append(0)
            else:
                ans.append(initial_window[0])
        return ans

o1=Solution()
ans=o1.firstNegInt([-8, 2, 3, -6, 10],2)
