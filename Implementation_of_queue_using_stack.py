class myQueue:

    def __init__(self):
        # Initialize your data members
        self.stack=[]
        
        
        

    def enqueue(self, x):
        # Implement the enqueue operation
        self.stack.append(x)
        
        
        
        
        
    def dequeue(self):
        # Implement the dequeue operation
        self.stack.pop(0)
        
        


    def front(self):
        # Return the front element of the queue
        if len(self.stack)!=0:
            return self.stack[0]
        else:
            return -1


    def size(self):
        # Return the current size of the queue
        return len(self.stack)
