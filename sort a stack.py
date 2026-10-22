class Solution:
    def sortStack(self, st):
        temp_stack=[]
        while len(st)>0:
            value=st.pop()
            if len(temp_stack)==0:
                temp_stack.append(value)
            elif value<temp_stack[-1]:
                while len(temp_stack)!=0 and value<temp_stack[-1]:
                    value_2=temp_stack.pop()
                    st.append(value_2)
                temp_stack.append(value)
            else:
                temp_stack.append(value)
        st.extend(temp_stack)
        return st
        
