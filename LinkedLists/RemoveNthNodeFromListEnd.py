# Given a linked list, remove the nth node from the end of list and return its head.

# For example,
# Given linked list: 1->2->3->4->5, and n = 2.
# After removing the second node from the end, the linked list becomes 1->2->3->5.

#  Note:
# If n is greater than the size of the list, remove the first node of the list.
# Try doing it using constant additional space.


# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param head : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def removeNthFromEnd(self, head, B):
        if not head:
            return head
        if not head.next:
            if B>=1:
                return None
            else:
                return head
        curr=head
        count=0
        while curr:
            count+=1
            curr=curr.next
        if B>=count :
            head=head.next
            return head
        k=0
        curr=head
        while k<count-B:
            prev=curr
            curr=curr.next
            k+=1
        prev.next=curr.next
        return head