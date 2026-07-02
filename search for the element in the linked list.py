class Solution:
    def searchKey(self, head, key):
        #Code here
        curr=head
        while curr is not None:
            if curr.data==key:
                return True
            curr=curr.next
        return False
            
