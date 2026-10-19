class Solution:
    def calculate(self, s: str) -> int:
        stack=[]
        num=0
        operator="+"
      
        for i in range(len(s)+1):
            if i == len(s):
                ch="+"
            else:
                ch=s[i]
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch!=" ":
                if operator=="+":
                    stack.append(num)
                elif operator=="-":
                    stack.append(-num)
                elif operator=="*":
                    stack.append(stack.pop()*num)
                elif operator=="/":
                  
                    stack.append(int(stack.pop()/num))
                operator=ch
                num=0
        return sum(stack)
