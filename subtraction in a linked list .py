class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def subLinkedList(self, head1, head2):  
        """Trim the leading zeros """
        head1 = self.ll_trimer(head1)
        head2 = self.ll_trimer(head2)

        """Finding the largest number"""
        l1_length = self.length(head1)
        l2_length = self.length(head2)

        if l1_length == l2_length:
            temp_1 = head1
            temp_2 = head2
            highest = None
            lowest = None
            flag = 0
            while temp_1 and temp_2:
                if temp_1.data > temp_2.data:
                    highest = head1
                    lowest = head2
                    flag = 1
                    break 
                elif temp_1.data < temp_2.data:
                    highest = head2
                    lowest = head1
                    flag = 1
                    break
                temp_1 = temp_1.next
                temp_2 = temp_2.next
            if flag == 0:
                return Node(0)
        elif l1_length > l2_length:
            highest = head1
            lowest = head2
        else:
            highest = head2
            lowest = head1

        reversed_highest = self.reverse_linked_list(highest)
        reversed_lowest = self.reverse_linked_list(lowest)

        """Now performing the subtraction in the reversed linked list """
        reversed_temp_highest = reversed_highest
        reversed_temp_lowest = reversed_lowest
        dummy = Node(-1)
        dummy_temp = dummy
        borrow = 0

        while reversed_temp_highest and reversed_temp_lowest:
            if reversed_temp_highest.data - borrow >= reversed_temp_lowest.data:
                ans = reversed_temp_highest.data - borrow - reversed_temp_lowest.data
                data_adder = Node(ans)
                dummy_temp.next = data_adder
                dummy_temp = data_adder
                reversed_temp_highest = reversed_temp_highest.next
                reversed_temp_lowest = reversed_temp_lowest.next
                borrow = 0
            else:
                ans = reversed_temp_highest.data - borrow + 10 - reversed_temp_lowest.data
                data_adder = Node(ans)
                dummy_temp.next = data_adder
                dummy_temp = data_adder
                reversed_temp_highest = reversed_temp_highest.next
                reversed_temp_lowest = reversed_temp_lowest.next
                borrow = 1

        while reversed_temp_highest:
            if reversed_temp_highest.data - borrow >= 0:
                ans = reversed_temp_highest.data - borrow
                borrow = 0
            else:
                ans = reversed_temp_highest.data - borrow + 10
                borrow = 1
            data_adder = Node(ans)
            dummy_temp.next = data_adder
            dummy_temp = data_adder
            reversed_temp_highest = reversed_temp_highest.next

        correct_ans = self.reverse_linked_list(dummy.next)
        trimmed_ans = self.ll_trimer(correct_ans)
        return trimmed_ans

    def ll_trimer(self, head1):
        curr = head1
        while curr and curr.data == 0:
            curr = curr.next
        if not curr:
            return Node(0)
        return curr

    def length(self, head):
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
        return count

    def reverse_linked_list(self, head):
        curr = head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
