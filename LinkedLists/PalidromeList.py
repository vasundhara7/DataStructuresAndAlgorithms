# Palindrome List
# Asked in:  
# Amazon
# Microsoft
# Given a singly linked list, determine if its a palindrome. Return 1 or 0 denoting if its a palindrome or not, respectively.

# Notes:

# Expected solution is linear in time and constant in space.
# For example,

# List 1-->2-->1 is a palindrome.
# List 1-->2-->3 is not a palindrome.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return an integer
    def lPalin(self, A):
        count=0
        if not A or not A.next:
            return 1
        curr=A
        
        while curr:
            count+=1
            curr=curr.next
        li=[]
        curr=A
        k=0
        while k<count//2:
            li.append(curr)
            curr=curr.next
            k+=1
        if count%2!=0:
            curr=curr.next
        while curr:
            x=li.pop()
            if x.val!=curr.val:
                return 0
            else:
                curr=curr.next
        return 1
