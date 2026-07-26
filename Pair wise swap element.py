''' Structure of linked list Node
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''
class Solution:
    def pairwiseSwap(self, head):
        swap_possible=0
        curr=head
        prev=None
        while curr:
            swap_possible+=1
            if swap_possible==2:
                temp_prev_data=prev.data
                prev.data=curr.data
                curr.data=temp_prev_data
                curr=curr.next
                swap_possible=0
                
            else:
                prev=curr
                curr=curr.next
        return head
                
                
        
