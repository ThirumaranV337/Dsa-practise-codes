'''Structure of a link list node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def countPairs(self, head1, head2, x):
        
        count=0
        curr_one=head1
        while curr_one:
            curr_two=head2
            while curr_two:
                if curr_one.data + curr_two.data ==x:
                    count+=1
                curr_two=curr_two.next
            curr_one=curr_one.next
        return count
##time complexity is o(n^2)
##space complexity is O(1)
