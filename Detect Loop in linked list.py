'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def detectLoop(self, head):
        hash_map=set()
        curr=head
        while curr:
            if curr in hash_map:
                return True
            else:
                hash_map.add(curr)
                curr=curr.next
        return False
