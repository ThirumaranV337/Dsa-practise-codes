import bisect
class Solution:
    def rowWithMax1s(self, arr):
        row=len(arr)
        column=len(arr[0])
        max=0
        index=-1
        for i in range(row):
            lower_bound=bisect.bisect_left(arr[i],1)
            count_1=column-lower_bound
            if count_1>max:
                max=count_1
                index=i
       
        return index
       
o1=Solution()
arr=[[0,0,1],[0,1,1],[0,0,0]]
ans=o1.rowWithMax1s(arr)
