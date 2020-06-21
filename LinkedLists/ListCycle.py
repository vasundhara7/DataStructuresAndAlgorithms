# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

# Try solving it using constant additional space.

# Example :

# Input : 

#                   ______
#                  |     |
#                  \/    |
#         1 -> 2 -> 3 -> 4

# Return the node corresponding to node 3. 


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head : head node of linked list
    # @return the first node in the cycle in the linked list
    def detectCycle(self, head):
        if not head or not head.next:
            return None
        slow=head
        fast=head
        slow=slow.next
        fast=fast.next.next
        
        while fast and fast.next: 
            if slow==fast:
                break
            
            slow=slow.next
            fast=fast.next.next
            
        if slow!=fast:
            return None
        slow=head
        while slow!=fast:
            
            slow=slow.next
            fast=fast.next
        return slow