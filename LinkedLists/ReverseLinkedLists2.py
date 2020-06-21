# Reverse a linked list from position m to n. Do it in-place and in one-pass.

# For example:
# Given 1->2->3->4->5->NULL, m = 2 and n = 4,

# return 1->4->3->2->5->NULL.

#  Note:
# Given m, n satisfy the following condition:
# 1 ≤ m ≤ n ≤ length of list. Note 2:
# Usually the version often seen in the interviews is reversing the whole linked list which is obviously an easier version of this question. 


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @param C : integer
    # @return the head node in the linked list
    def reverseBetween(self, A, B, C):
        if not A:
            return A
        if B==C:
            return A
        count=0
        curr=A
        prev=A
        while count<B-1:
            prev=curr
            curr=curr.next
            count+=1
        prev_link=prev
        tail_link=curr
        prev=curr
        curr=curr.next
        while count<C-1:
            after=curr.next
            curr.next=prev
            prev=curr
            curr=after
            count+=1
        if B==1:
            A=prev
        else:
            prev_link.next=prev
        tail_link.next=curr
        
        return A