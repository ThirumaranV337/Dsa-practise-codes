# Node class
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

# Queue class template
class myQueue:
    def __init__(self):
        # Initialize your data members
        self.head=None

    def isEmpty(self):
        # Return True if queue is empty, else False
        if self.head:
            return False
        return True
        
        
    def enqueue(self, x):
        # Add element x to the rear
        if self.head==None:
            self.head=Node(x)
        else:
            curr=self.head
            while curr.next:
                curr=curr.next
            curr.next=Node(x)    
        
    def dequeue(self):
        # Remove the front element
        if self.head:
            self.head=self.head.next

    def getFront(self):
        # Return front element
        # return -1 if empty
        if self.head:
            return self.head.data
        else:
            return -1


            
        

    def size(self):
        # Return current size
        count=0
        if self.head:
            curr=self.head
            while curr.next:
                count+=1
                curr=curr.next
            return count+1
        return count
                
