class Solution:
    def calculate(self, s: str) -> int:
        operator=[]
        operand=[]
        priority={"*":3,"/":3,"+":2,"-":2}
        for i in s:
            if i in{"+","-","*","/"}:
                operator.append(i)
            elif i ==" ":
                continue
            else:
                val=int(i)
                operand.append(val)

        if len(operator)==0:
            return int(s)
        for j in operator:
            if j=="*":
                value_1=operand.pop()
                value_2=operand.pop()
                ans=value_1*value_2
                operand.append(ans)
                operator.remove(j)
            elif j=="/":
                value_1=operand.pop()
                value_2=operand.pop()
                ans=value_2//value_1
                operand.append(ans)
                operator.remove(j)
            
        for k in operator:
            if k=="+":
                value_1=operand.pop()
                value_2=operand.pop()
                ans=value_1+value_2
                operand.append(ans)
                operator.remove(k)
            elif j=="-":
                value_1=operand.pop()
                value_2=operand.pop()
                ans=value_1-value_2
                operand.append(ans)
                operator.remove(k)
            
        return operand[-1]
