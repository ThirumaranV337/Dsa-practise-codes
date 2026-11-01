def countMinReversals(s):
    if len(s)%2==1:
        return -1
    # Code Here
    stack=[]
    count=0
    for i in s:
        if i=="{":
            stack.append(i)
        elif i=="}":
            if len(stack)==0:
                
                count+=1
                stack.append("{")
                
                
            else:
                stack.pop()
    ans=count+(len(stack)//2)
    return ans
