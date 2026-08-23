
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
        self.random = None
       

class Solution:
    def cloneLinkedList(self, head):
        hash_map={}
        """save the old value as the key and the nw value as value for the fast retrival """
        curr=head
        while curr:
            new_node=Node(curr.data)
            hash_map[curr]=new_node
            curr=curr.next
        
        curr=head
        while curr:
            new_value=hash_map.get(curr)
            ##checking the random pointer
            random_pointer=hash_map.get(curr.random)
            new_value.random=random_pointer
            next_pointer=hash_map.get(curr.next)
            new_value.next=next_pointer
            curr=curr.next
        return hash_map[head]
            
            
            
    
