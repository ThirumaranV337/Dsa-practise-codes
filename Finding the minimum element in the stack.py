class SpecialStack:

    def __init__(self):
        self.stack=[]
        
        
        
        
    
    def push(self, x):
        
        self.stack.append(x)
        
            
    
    def pop(self):
        # Remove the top element from the Stack
        if len(self.stack)!=0:
            self.stack.pop()
        else:
            return -1

    
    def peek(self):
        # Returns top element of Stack
        if len(self.stack)!=0:
            return self.stack[-1]
        else:
            return -1
        
    def isEmpty(self):
        if len(self.stack)==0:
            return True
        else:
            return False

    
    def getMin(self):
        # Finds minimum element of Stack
        if len(self.stack)!=0:
            return min(self.stack)
        else:
            return -1
