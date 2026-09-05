
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None

class Solution:
    def reverse(self, head):
        curr=head
        temp=None
        while curr:
            temp=curr.prev
            curr.prev=curr.next
            curr.next=temp
            curr=curr.prev
        return temp.prev


      """
      time complexity o(n)
      space complexity o(1)
      """
            
