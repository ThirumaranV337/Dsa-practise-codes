
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def addOne(self,head):
        reverse_head=self.reverse(head)
        carry=1
        curr=reverse_head
        while curr and carry==1:
            curr.data+=carry
            if curr.data >= 10:
                curr.data=0
                carry=1
                curr=curr.next
            else:
                carry=0
                curr=curr.next
        if carry==1:
            reversed_head2=self.reverse(reverse_head)
            new_node=Node(carry)
            new_node.next=reversed_head2
            return new_node
        else:
            reversed_head2=self.reverse(reverse_head)
            return reversed_head2
    def reverse(self,head):
        curr=head
        front=head.next
        prev=None
        while curr:
            curr.next=prev
            prev=curr
            curr=front
            if curr:
                front=curr.next
        return prev
