class Solution:
    def calculateSpan(self, arr):
        stack=[]
        
        span=[]
        result=[]
        for i in arr:
            if len(stack)==0:
                stack.append(i)
                result.append(1)
                span.append(1)
            elif i<stack[-1]:
                stack.append(i)
                result.append(1)
                span.append(1)
            else:
                value=0
                while len(stack)!=0 and i>=stack[-1] :
                    value+=span[-1]
                    stack.pop()
                    span.pop()
                    
                value+=1
                stack.append(i)
                result.append(value)
                span.append(value)
        return result
                
                
        
