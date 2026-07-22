'''
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None
'''

class Solution:
    def lengthOfLoop(self, head):
        slow=head
        fast=head.next
        while fast and fast.next:
            if fast==slow:
                curr_l=fast.next
                count=1
                while curr_l:
                    if curr_l!=slow:
                        count+=1
                        curr_l=curr_l.next
                    else:
                        return count
        
                        
            else:
                slow=slow.next
                fast=fast.next.next
        return 0
            
            
                
            
