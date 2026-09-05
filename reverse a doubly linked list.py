
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None

class Solution:
    def reverse(self, head):
        stack=[]
        curr=head
        while curr:
            stack.append(curr)
            curr=curr.next
        dummy=Node(-1)
        temp=dummy
        previous=None
        for i in range(len(stack)):
            curr_node=stack.pop()
            temp.next=curr_node
            curr_node.prev=previous
            previous=curr_node
            temp=temp.next
        temp.next=None   
        return dummy.next
        
            
            
