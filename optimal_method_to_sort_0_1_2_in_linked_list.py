
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

	
class Solution:
    def segregate(self, head):
        """I am using the dumy Linked list for each data type then I coneecting them"""
        zeros_dummy=Node(-1)
        zeros_pointer=zeros_dummy
        ones_dummy=Node(-1)
        ones_pointer=ones_dummy
        twos_dummy=Node(-1)
        twos_pointer=twos_dummy
        
        """ Splitting the linked list into the multiple dummy nodes and then connecting it """
        curr=head
        while curr:
            if curr.data==0:
               zeros_pointer.next=curr
               zeros_pointer=curr
               curr=curr.next
            elif curr.data==1:
                ones_pointer.next=curr
                ones_pointer=curr
                curr=curr.next
            elif curr.data==2:
                twos_pointer.next=curr
                twos_pointer=curr
                curr=curr.next
        if ones_dummy.next:
            zeros_pointer.next=ones_dummy.next
            ones_pointer.next=twos_dummy.next
        else:
            zeros_pointer.next=twos_dummy.next
            
        twos_pointer.next = None   
        return zeros_dummy.next
        
        
            
            
                
                
               
                
        
        
        
        
