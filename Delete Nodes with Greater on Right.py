
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

class Solution:
    def compute(self,head):
        ##reversing the linked list
        reveresed_head=self.ll_reverser(head)
        
        """Assigning the first value as maximum becuse when 
        you deeply see the all the test case you can able 
        to notice the list value always remain same because 
        there is no right element to compare """
        max_value=reveresed_head.data
        prev=reveresed_head
        curr=reveresed_head.next
        while curr:
            if curr.data>=max_value:
                max_value=curr.data
                prev=curr
                curr=curr.next
                
                
            elif curr.data<max_value:
                prev.next=curr.next
                curr=curr.next
                
        original=self.ll_reverser(reveresed_head)
        return original 
                
        
    def ll_reverser(self,head):
        curr=head
        prev=None
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        return prev
        
        
