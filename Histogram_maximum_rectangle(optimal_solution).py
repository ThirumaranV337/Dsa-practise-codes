class Solution:
    def getMaxArea(self, arr):
        length=len(arr)
        left_min=[]
        right_min=[]
        stack_1=[]
        stack_2=[]
        for i in range(length):
            if len(stack_1)==0:
                left_min.append(0)
                stack_1.append(i)
            elif arr[i]>arr[stack_1[-1]]:
                left_min.append(stack_1[-1]+1)
                stack_1.append(i)
            elif arr[i]<=arr[stack_1[-1]]:
                while len(stack_1)>0 and arr[i]<=arr[stack_1[-1]]:
                    stack_1.pop()
                if len(stack_1)==0:
                    stack_1.append(i)
                    left_min.append(0)
                else:
                    left_min.append(stack_1[-1]+1)
                    stack_1.append(i)
        for j in range(length-1,-1,-1):
            if len(stack_2)==0:
                right_min.append(length-1)
                stack_2.append(j)
            elif arr[j]>arr[stack_2[-1]]:
                right_min.append(stack_2[-1]-1)
                stack_2.append(j)
            elif arr[j]<=arr[stack_2[-1]]:
                while len(stack_2)>0 and arr[j]<=arr[stack_2[-1]]:
                    stack_2.pop()
                if len(stack_2)==0:
                    stack_2.append(j)
                    right_min.append(length-1)
                else:
                    right_min.append(stack_2[-1]-1)
                    stack_2.append(j)

        right_min=right_min[::-1]
        ans=[]
        for k in range(length):
            value=(right_min[k]-left_min[k]+1)*arr[k]
            ans.append(value)
        return max(ans)
        


                
