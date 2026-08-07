
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None   

class Solution:
    def divide(self, head):
        odd_container=Node(-1)
        temp_odd=odd_container
        even_container=Node(-1)
        temp_even=even_container
        curr=head
        while curr:
            if curr.data%2 == 0:
                temp_even.next=curr
                temp_even=temp_even.next
                curr=curr.next
            else:
                temp_odd.next=curr
                temp_odd=temp_odd.next
                curr=curr.next
        temp_even.next=None
        temp_odd.next=None
         
        temp_even.next=odd_container.next
        return even_container.next

                
                
                
                
                
        
