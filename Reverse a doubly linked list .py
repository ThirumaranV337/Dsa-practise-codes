""" Structure of Doubly Linked List Node
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
"""

class Solution:
    def reverse(self, head):
        stack=[]
        curr=head
        while curr:
            stack.append(curr.data)
            curr=curr.next
        curr=head
        while curr:
            data=stack.pop()
            curr.data=data
            curr=curr.next
        return head
