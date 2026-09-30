class Solution:
    def getMaxArea(self, arr):
        length=len(arr)
        total_ans=[]
        for i in range(length):
            count_back=0
            count_front=0
            for j in range(i+1,length):
                if arr[i]<=arr[j]:
                    count_front+=1
                else:
                    break
            for k in range(i-1,-1,-1):
                if arr[i]<=arr[k]:
                    count_back+=1
                else:
                    break
            total_count=count_front+count_back+1
            ans=total_count*arr[i]
            total_ans.append(ans)
         
