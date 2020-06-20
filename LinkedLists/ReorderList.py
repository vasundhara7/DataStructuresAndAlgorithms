# Given a singly linked list

#     L: L0 → L1 → … → Ln-1 → Ln,
# reorder it to:

#     L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …
# You must do this in-place without altering the nodes’ values.

# For example,
# Given {1,2,3,4}, reorder it to {1,4,2,3}.

# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reorderList(self, head):
        if not head or not head.next:
            return head
        ptr1=head
        ptr2=head
        while ptr2 and ptr2.next:
            prev=ptr1
            ptr1=ptr1.next
            ptr2=ptr2.next.next
        l2=ptr1
        prev.next=None
        l2=self.reverse(l2)
        
        
        l1=head
        k=0
        curr=head
        after2=l2
        while curr:
            if k%2==0:
                after1=curr.next
                
                curr.next=after2
                curr=curr.next
            else:
                after2=curr.next
                if after1:
                    curr.next=after1
                else:
                    return head
                curr=curr.next
            k+=1
        return head
    
    def reverse(self,head):
        prev=None
        curr=head
        after=None
        while curr:
            after=curr.next
            curr.next=prev
            prev=curr
            curr=after
        head=prev
        return head
        
            