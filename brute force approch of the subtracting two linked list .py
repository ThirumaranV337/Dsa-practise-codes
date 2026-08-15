class Node:
    def __init__(self,data):
        self.data=data
        self.Next=None


class Solution:
    def subLinkedList(self, head1, head2):  
        number_1_str=self.linked_list_string(head1)
        number_2_str=self.linked_list_string(head2)
        integer_1=int(number_1_str)
        integer_2=int(number_2_str)
        result=abs(integer_1-integer_2)
        result_str=str(result)
        result_dummy=Node(-1)
        curr=result_dummy
        for data in result_str:
            integer_add=int(data)
            adder_node=Node(integer_add)
            curr.next=adder_node
            curr=adder_node
        return result_dummy.next 
        
        
        pass
    def linked_list_string(self,head):
        number_str=""
        curr=head
        while curr:
            num_to_add=str(curr.data)
            number_str+=num_to_add
            curr=curr.next
        return number_str
            
            
      
        
