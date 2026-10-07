class Solution:
    def evaluatePostfix(self, arr):
       stack=[]
       value_1=None
       value_2=None
       for i in arr:
           if  i in {"+","-","*","/","^"}:
               value_1=stack.pop()
               value_2=stack.pop()
               if i=="+":
                   adding_value=value_1+value_2
               elif i=="-":
                   adding_value=value_2-value_1
               elif i=="*":
                   adding_value=value_1*value_2
               elif i=="/":
                   adding_value=value_2//value_1
               elif i=="^":
                   adding_value=value_2**value_1
               stack.append(adding_value)
           else:
                stack.append(int(i))
       return stack[-1]
               
        
