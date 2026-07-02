class Node:
    """Here we are creating the template of the Node """
    def __init__(self,data):
        self.data=data
        self.pointer=None
class Linked_list():
    """Here we are creating the template of the linked list """
    def __init__(self):
        self.head=None
        self.tail=None
        """Adding the element through this function"""
    def add_element(self,data):
        """Using the node template for this linked list """
        element_value=Node(data)
        if self.head==None:
            """
            when we are creating the first node we want to kept it as both head and as tail 
            """
            self.head=element_value
            self.tail=element_value
        else:
            """
            when the head is not none we want to add the element after the head and we assign it as a tail 
            """
            self.tail.pointer=element_value
            self.tail=element_value
    def print_linked_list(self):
        curr=self.head
        while curr is not  None:
            
            print(curr.data,end=" ")
            curr=curr.pointer
        

Linked_list_1=Linked_list()
Linked_list_1.add_element(10)
Linked_list_1.add_element(20)
Linked_list_1.print_linked_list()



      

