class Solution:
    def reducedString(self, k, s):
        stack=[]
        for ch in s:
            if stack and stack[-1][0]==ch:
                ##here we are overwriting the already existed stack values
                stack[-1]=(ch,stack[-1][1]+1)
            else:
                stack.append((ch,1))
            if stack[-1][1]==k:
                stack.pop()
        ans=""
        for i in range(len(stack)):
            ans += stack[i][0] * stack[i][1]##the stack vlues is overrided so using the count value we make it as repetable if that is repeated 
            
        return ans
            
                
