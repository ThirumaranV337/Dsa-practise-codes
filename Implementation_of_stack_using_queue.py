from collections import deque

class myStack:

    def __init__(self):
        self.q = deque()

    def push(self, x):
        # push element on top
        self.q.appendleft(x)
        
    def pop(self):
        # remove top element
        if len(self.q)!=0:
            self.q.popleft()
        else:
            return -1
        
    def top(self):
        # return top element
        if len(self.q)!=0:
            value=self.q[0]
            return value
        else:
            return -1
        
        
        
    def size(self):
        # return current size
        return len(self.q)
        
