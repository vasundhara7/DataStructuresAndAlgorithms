# Merge two sorted linked lists and return it as a new list.
# The new list should be made by splicing together the nodes of the first two lists, and should also be sorted.

# For example, given following linked lists :

#   5 -> 8 -> 20 
#   4 -> 11 -> 15
# The merged list should be :

# 4 -> 5 -> 8 -> 11 -> 15 -> 20

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def mergeTwoLists(self, A, B):
        if not A or not B:
            if not A:
                return B
            else:
                return A
        
        if A.val<B.val:
            head=A
            
            curr1=A.next
            curr2=B
        else:
            head=B
            curr1=B.next
            curr2=A
        curr=head
        while curr1 and curr2:
            if curr1.val>curr2.val:
                
                curr.next=curr2
                curr=curr.next
                curr2=curr2.next
            else:
                
                curr.next=curr1
                curr=curr.next
                curr1=curr1.next
        
        if curr1:
            curr.next=curr1
            curr1=curr1.next
            curr=curr.next
        if curr2:
            curr.next=curr2
            curr2=curr2.next
            curr=curr.next
        return head
                