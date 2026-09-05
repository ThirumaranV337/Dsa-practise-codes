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
        map_value_checker=set()
        map_added_checker=set()
        curr=head
        while curr:
            map_value_checker.add(curr.data)
            curr=curr.next
            
        curr=head
        returning_list=[]
        
        while curr:
            value=target-curr.data
            if value in map_value_checker and value not in map_added_checker:
                if value==curr.data:
                    curr=curr.next
                    pass
                else:
                    list_add=[curr.data,value]
                    returning_list.append(list_add)
                    map_added_checker.add(value)
                    map_added_checker.add(curr.data)
                    curr=curr.next
            else:
                curr=curr.next
        return returning_list
                
                
            
                
                
        
        
