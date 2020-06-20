# Given a list, rotate the list to the right by k places, where k is non-negative.

# For example:

# Given 1->2->3->4->5->NULL and k = 2,
# return 4->5->1->2->3->NULL.

# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def rotateRight(self, A, B):
        length=0
        if not A or not A.next:
            return A
        curr=A
        while curr:
            length+=1
            tail=curr
            curr=curr.next
        val=B%length
        if val==0:
            return A
        count=0
        curr=A
        while count<length-val:
            count+=1
            prev=curr
            curr=curr.next
            
        prev.next=None
        tail.next=A
        A=curr
        return A