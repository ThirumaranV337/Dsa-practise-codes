'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
	
class Solution:
    def segregate(self, head):
        """performing the count of the 0,1,2 then doing the data replacement """
        count_0=0
        count_1=0
        count_2=0
        curr=head
        while curr:
            if curr.data==0:
                count_0+=1
                curr=curr.next
            elif curr.data==1:
                count_1+=1
                curr=curr.next
            else:
                count_2+=1
                curr=curr.next
        curr=head
        while curr:
            if count_0!=0:
                curr.data=0
                count_0-=1
                curr=curr.next
            elif count_1!=0:
                curr.data=1
                count_1-=1
                curr=curr.next
            elif count_2!=0:
                curr.data=2
                count_2-=1
                curr=curr.next
        return head
        
                
            
        
        
        
    
