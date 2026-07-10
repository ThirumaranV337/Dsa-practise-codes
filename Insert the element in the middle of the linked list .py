'''
structure of a linked list node 
'''
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


import math
class Solution:
    def insertInMiddle(self, head, x):
        length=self.length_linked_list(head)
        middle=math.ceil(length/2)
        curr=head
        count=0
        while count<middle-1: ##reducing the out of range by using the middle -1 
            count+=1
            curr=curr.next
        new_node=Node(x)
        if curr is not None:
            new_node.next=curr.next
            curr.next=new_node
            return head
        return new_node##handeled the head is empty 
        
        
        
        
            
        
    """Function to find the length of the linked list """
    def length_linked_list(self,head):
        curr=head
        count=0
        while curr:
            count+=1
            curr=curr.next
        return count
        

        
