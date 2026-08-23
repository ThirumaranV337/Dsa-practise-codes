

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class Solution:

    def deleteAllOccurances(self, head, x):
        dummy=Node(-1)
        temp_dummy=dummy
        curr=head
        while curr:
            if curr.data != x:
                temp_dummy.next=curr
                temp_dummy=curr
                curr=curr.next
            else:
                curr=curr.next
        temp_dummy.next=None
        return dummy.next
        
