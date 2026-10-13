class Solution:
    def preToPost(self, s):
        stack=[]
        for i in range(len(s)-1,-1,-1):
            if s[i] in{"/","-","*","+"}:
                value_1=stack.pop()
                value_2=stack.pop()
                new_value=value_1
                new_value+=value_2
                new_value+=s[i]
                stack.append(new_value)
            else:
                stack.append(s[i])
        return stack[-1]
                
                
            
                
                
        
