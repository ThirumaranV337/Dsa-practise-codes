
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def addTwoLists(self, head1, head2):
        length_1=self.length(head1)
        length_2=self.length(head2)
        if length_1==1 and length_2==1 and head1.data==0 and head2.data==0:
            return head1
        
        head_1_reverse=self.reverse(head1)
        head_2_reverse=self.reverse(head2)
        dummy=Node(-1)
        temp_dummy=dummy
        temp_1=head_1_reverse
        temp_2=head_2_reverse
        sum_val=0
        carry=0
        while temp_1 and temp_2:
            sum_val=temp_1.data+temp_2.data+carry
            if sum_val>=10:
                data_add=sum_val%10
                carry=sum_val//10
                new_node=Node(data_add)
                temp_dummy.next=new_node
                temp_dummy=new_node
                temp_1=temp_1.next
                temp_2=temp_2.next
            else:
                carry=0
                new_node=Node(sum_val)
                temp_dummy.next=new_node
                temp_dummy=new_node
                temp_1=temp_1.next
                temp_2=temp_2.next
        if temp_1:
            curr=temp_1
            while curr:
                sum_val=curr.data+carry
                data_add=(sum_val%10)
                carry=sum_val//10
                new_node=Node(data_add)
                temp_dummy.next=new_node
                temp_dummy=new_node
                curr=curr.next
        elif temp_2:
            curr=temp_2
            while curr:
                sum_val=curr.data+carry
                data_add=(sum_val%10)
                carry=sum_val//10
                new_node=Node(data_add)
                temp_dummy.next=new_node
                temp_dummy=new_node
                curr=curr.next
        elif carry > 0:
            new_node=Node(carry)
            temp_dummy.next=new_node
            temp_dummy=new_node
            
            
        reversed_return=self.reverse(dummy.next)
        correct=self.remove_leading_zero(reversed_return)
        return correct 
    def reverse(self,head):
        curr=head
        front=head.next
        prev=None
        while curr:
            curr.next=prev
            prev=curr
            curr=front
            if curr:
                front=curr.next
        return prev
    def remove_leading_zero(self,head):
        curr=head
        while curr:
            if curr.data==0:
                curr=curr.next
            else:
                return curr
    def length(self,head):
        count=0
        curr=head
        while curr:
            count+=1
            curr=curr.next
        return count
        
        
        
