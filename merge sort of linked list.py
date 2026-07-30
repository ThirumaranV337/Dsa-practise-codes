
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def mergeSort(self, head):
        if  head and not head.next:
            return head
        mid=self.find_mid(head)
        left_head=head
        right_head=mid.next
        mid.next=None
        left=self.mergeSort(left_head)
        right=self.mergeSort(right_head)
        return self.sortedMerge(left,right)
    def sortedMerge(self, head1, head2):
        curr_1=head1
        curr_2=head2
        dummy_node=Node(-1)
        temp=dummy_node
        while curr_1 and curr_2:
            if curr_1.data>=curr_2.data:
                temp.next=curr_2
                temp=temp.next
                curr_2=curr_2.next
            elif curr_2.data>=curr_1.data:
                temp.next=curr_1
                temp=temp.next
                curr_1=curr_1.next
        if not curr_1:
            temp.next=curr_2
        else:
            temp.next=curr_1
        return dummy_node.next
        
        
      
    def find_mid(self,head):
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow
        
            
            
            
        
