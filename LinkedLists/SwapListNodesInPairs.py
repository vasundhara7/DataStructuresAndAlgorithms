# Given a linked list, swap every two adjacent nodes and return its head.

# For example,
# Given 1->2->3->4, you should return the list as 2->1->4->3.

# Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.


# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        prev=None
        curr=head
        after=curr.next
        count=0
        while curr:
            if not after:
                curr.next=None
                return head
            curr.next=after.next
            after.next=curr
            if count==0:
                head=after
                
            else:
                prev.next=after
            prev=curr
            curr=curr.next
            if not curr:
                return head
            after=curr.next
            count+=1
        return head
