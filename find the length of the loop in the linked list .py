'''
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None
'''

class Solution:
    def lengthOfLoop(self, head):
        hash_map={}
        curr=head
        lengther=1
        
        while curr:
            if curr in hash_map:
                length=hash_map[curr]
                linked_list_length=lengther-length
                return linked_list_length
            else:
                hash_map[curr]=lengther
                curr=curr.next
                lengther+=1
        return 0
                
                
                
                
            
