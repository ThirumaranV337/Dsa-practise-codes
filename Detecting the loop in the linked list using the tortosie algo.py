'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def detectLoop(self, head):
        slow=head
        fast=head.next
        while fast and fast.next:
            if fast==slow:
                return True
            else:
                slow=slow.next
                fast=fast.next.next
        return False
""" time complexity is o(n)
    Space complexity is o(1)"""
