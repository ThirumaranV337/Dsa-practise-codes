"""Structure of a linked list node
class node:
    def __init__(self):
        self.data = None
        self.next = None
"""
class Solution:
    def maxPalindrome(self,head):
        curr=head
        Next=None
        prev=None
        result=1
        while curr:
            Next=curr.next
            curr.next=prev
            result=max(result,2*(self.count_finder(prev,Next))+1)
            result=max(result,2*(self.count_finder(curr,Next)))
            prev=curr
            curr=Next
        return result
        
    def count_finder(self,head1,head2):
        count=0
        while head1 and head2:
            if head1.data == head2.data:
                count+=1
            else:
                break
            head1=head1.next
            head2=head2.next
        return count
                    
            
            
        
       
    
        
        
        
            
        
