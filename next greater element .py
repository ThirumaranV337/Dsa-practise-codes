class Solution:
    def nextLargerElement(self, arr):
        # code here
        stack=[]
        return_list=[]
        for i in range(len(arr)-1,-1,-1):
            if len(stack)==0:
                return_list.append(-1)
                stack.append(arr[i])
            elif arr[i]<stack[-1]:
                return_list.append(stack[-1])
                stack.append(arr[i])
            elif arr[i]>=stack[-1]:
                while len(stack)!=0 and arr[i]>=stack[-1]:
                    stack.pop()
                if len(stack)==0:
                    return_list.append(-1)
                    stack.append(arr[i])
                elif arr[i]<stack[-1]:
                    return_list.append(stack[-1])
                    stack.append(arr[i])


        reversed_list = return_list[::-1] 
        return reversed_list
o1=Solution()
arr=[20, 18, 8, 17, 20, 20, 7, 2, 9, 10, 2, 11, 20, 8]
ans=o1.nextLargerElement(arr)
