
class Node:
     ##cresting the node template 
    def __init__(self, x):
        self.data = x
        self.next = None


class Solution:
    ##initializing the head for the linked list 
    def __init__(self):
        self.head=None
    def add_element_ll(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
        else:
             
            curr=self.head
            while curr.next:
                curr=curr.next
            curr.next=new_node
            return self.head
    def makeUnion(self, head1, head2):
        my_set={}
        self.add_element(head1,my_set)
        self.add_element(head2,my_set)
        return_head=None
        for node in my_set.keys():
            return_head=self.add_element_ll(node)
        return return_head    
            
        
        
    def add_element(self,head,my_set):
        curr=head
        while curr:
            my_set[curr.data]=True
            curr=curr.next
            
            
        
