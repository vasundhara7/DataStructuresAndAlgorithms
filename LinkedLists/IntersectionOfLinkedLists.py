# Write a program to find the node at which the intersection of two singly linked lists begins.

# For example, the following two linked lists:


# A:          a1 → a2
#                    ↘
#                      c1 → c2 → c3
#                    ↗
# B:     b1 → b2 → b3

# begin to intersect at node c1.

#  Notes:
# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function returns.
# You may assume there are no cycles anywhere in the entire linked structure.
# Your code should preferably run in O(n) time and use only O(1) memory.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def getIntersectionNode(self, A, B):
        if not A or not B:
            return None
        l1=A
        l2=B
        count1=0
        count2=0
        while l1.next or l2.next:
            if l1.next and l2.next:
                count1+=1
                count2+=1
                l1=l1.next
                l2=l2.next
            elif l1.next:
                count1+=1
                l1=l1.next
            else:
                count2+=1
                l2=l2.next
        if l1!=l2:
            return None
        l1=A
        l2=B
        if count1>count2:
            while count1>count2:
                l1=l1.next
                count1-=1
        elif count1<count2:
            while count2>count1:
                l2=l2.next
                count2-=1
        while l1:
            if l1==l2:
                return l1
            l1=l1.next
            l2=l2.next
            