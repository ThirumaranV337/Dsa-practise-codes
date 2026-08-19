
class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
class Solution:
    def flatten(self, head):
       if  head is None or head.next is None:
           return head
       merged=self.flatten(head.next)
       return self.merge_linked_list(merged,head)
    
    def merge_linked_list(self,head1,head2):
        dummy=Node(-1)
        temp_dummy=dummy
        while head1 and head2:
            if head1.data <=head2.data:
                temp_dummy.bottom=head1
    
                head1=head1.bottom
    
            else:
                temp_dummy.bottom=head2
                
                head2=head2.bottom
                
            temp_dummy=temp_dummy.bottom
            temp_dummy.next==None
        if head1:
            
            temp_dummy.bottom=head1
        elif head2:
            
            temp_dummy.bottom=head2
        return dummy.bottom
              
            
                
                
                
                
                
           
                
                
                
        
        
