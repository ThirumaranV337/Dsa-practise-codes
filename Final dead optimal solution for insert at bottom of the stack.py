class Solution:
    def insertAtBottom(self, st, x) :
        if len(st)==0:
            st.append(x)
            return st
        top=st.pop()
        self.insertAtBottom(st,x)
        st.append(top)
        
        return st
