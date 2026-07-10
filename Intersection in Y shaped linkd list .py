'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''

class Solution:
    def intersectPoint(self, head1, head2):
        map_store=set()
        curr_1=head1
        while curr_1:
            map_store.add(curr_1)
            curr_1=curr_1.next
        curr_2=head2
        while curr_2:
            if curr_2 in map_store:
                return curr_2
            else:
                curr_2=curr_2.next
        return None
            
