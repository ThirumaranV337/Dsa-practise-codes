''' Structure of linked list Node
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

'''
class Solution:
    def removeDuplicates(self, head):
        hash_map=set()
        prev=None
        curr=head
        while curr:
            if curr.data in hash_map:
                prev.next=curr.next
                curr=curr.next
            else:
                prev=curr
                hash_map.add(curr.data)
                curr=curr.next
        return head
