# Structure of Doubly Linked List Node
'''
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
'''

class Solution:
    def givenSumPairs(self, head, target):
        return_array=[]
        high=self.find_tail(head)
        low=head
        while low.data<high.data:
            value=low.data+high.data
            if value==target:
                return_array.append([low.data,high.data])
                high=high.prev
                low=low.next
            elif value>target:
                high=high.prev
            else:
                low=low.next
        return return_array
        
    def find_tail(self,head):
        curr=head
        previous=None
        while curr:
            previous=curr
            curr=curr.next
            
        return previous
                
            
                
                
        
        
