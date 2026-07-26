''' Structure of a Linked List node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def mergeSort(self, head):
        
        Linked_list_data=[]
        curr=head
        while curr:
            data=curr.data
            Linked_list_data.append(data)
            curr=curr.next
        Linked_list_data.sort()
        curr=head
        while curr:
            data=Linked_list_data[0]
            Linked_list_data.remove(data)
            curr.data=data
            curr=curr.next
        return head
            
            
            
        
