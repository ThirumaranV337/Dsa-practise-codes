'''Structure of a link list node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Solution:
    def countPairs(self, head1, head2, x):
        
        checker_set=set()
        curr=head1
        while curr:
            checker_set.add(curr.data)
            curr=curr.next
        curr=head2
        count=0
        while curr:
            checker_value=x-curr.data
            if checker_value in checker_set:
                count+=1
            curr=curr.next
        return count
            
            
