class myQueue:
    def __init__(self, n):
        # Define Data Structures
        self.queue=[]
        self.n=n
    def isEmpty(self):
        # Check if queue is empty
        if len(self.queue)==0:
            return True
        return False

    def isFull(self):
        # Check if queue is full
        if len(self.queue)==self.n:
            return True
        return False

    def enqueue(self, x):
        # Enqueue
        if len(self.queue)<self.n:
            
            self.queue.append(x)

    def dequeue(self):
        # Dequeue
        self.queue.pop(0)

    def getFront(self):
        # Get front element
        if len(self.queue)!=0:
            return self.queue[0]
        return -1

    def getRear(self):
        # Get rear element 
        if len(self.queue)!=0:
            return self.queue[-1]
        return -1
        
        
