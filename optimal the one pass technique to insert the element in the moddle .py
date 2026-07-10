'''
structure of a linked list node 
'''
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None



class Solution:
    def insertInMiddle(self, head, x):
        middle_node=self.middle_linked_list(head)
        new_node=Node(x)
        if not head:
            return new_node
        new_node.next=middle_node.next
        middle_node.next=new_node
        return head
    def middle_linked_list(self,head):
        slow=head
        fast=head
        while fast and fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        return slow
        
        

        
