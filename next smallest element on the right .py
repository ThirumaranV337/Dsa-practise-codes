def nextSmallerElement(arr,n):
    # Write your code here.
    stack=[]
    ans=[]
    for i in range(n-1,-1,-1):
        if len(stack)==0:
            ans.append(-1)
            stack.append(arr[i])
        elif arr[i]>stack[-1]:
            ans.append(stack[-1])
            stack.append(arr[i])
        elif arr[i]<=stack[-1]:
            while len(stack)!=0 and arr[i]<=stack[-1]:
                stack.pop()
            if len(stack)==0:
                ans.append(-1)
                stack.append(arr[i])
            elif arr[i]>stack[-1]:
                ans.append(stack[-1])
                stack.append(arr[i])

    final_ans=ans[::-1]
    return final_ans
