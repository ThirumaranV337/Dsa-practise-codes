"""
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        """


class Solution:
    def reverseList(self, head):
        curr=head""" Initilizing the current pointer as head"""
        prev=None
        while curr is not None:
            front=curr.next##from the current point looking for the next 
            curr.next=prev##changing the direction of the pointer 
            prev=curr##storing the curr as previous for the next pointer
            curr=front##then now moving to the next node 
        return prev
        
"""
time complexity o(n)
space complexity o(1)
"""
                
      
        
       
        
      
        
