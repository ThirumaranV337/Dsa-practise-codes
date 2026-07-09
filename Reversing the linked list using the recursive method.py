"""
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        """


class Solution:
    def reverseList(self, head):
        """This statement is returning the head if it is single """
       if head == None or head.next == None:
           return head
       """starting from the tail we looking backward to reverse and changing the pointer recursively"""
       newhead=self.reverseList(head.next)
       front=head.next##in this recursive method the previous is the front because we are looking from the backward 
       front.next=head
       head.next=None
       return newhead
        
"""
time complexity o(n)
space complexity o(1)
"""
                
      
        
       
        
      
        
