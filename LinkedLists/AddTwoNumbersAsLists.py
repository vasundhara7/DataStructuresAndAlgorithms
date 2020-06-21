# You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

#     342 + 465 = 807
# Make sure there are no trailing zeros in the output list
# So, 7 -> 0 -> 8 -> 0 is not a valid response even though the value is still 807.

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addTwoNumbers(self, A, B):
        if not A or not B:
            if not A:
                return B
            else:
                return A
        
        
        carry=0
        num1=A
        num2=B
        s=num1.val+num2.val
        head=ListNode(s%10)
        num1=num1.next
        num2=num2.next
        if s>9:
            carry=1
        curr=head
        while num1 or num2:
            if num1 and num2:
                
                s=carry+num1.val+num2.val
                num1=num1.next
                num2=num2.next
            elif num1:
                s=carry+num1.val
                num1=num1.next
            else:
                s=carry+num2.val
                num2=num2.next
            digit=s%10
            if s>9:
                carry=1
            else:
                carry=0
            curr.next=ListNode(digit)
            curr=curr.next
        if carry==1:
            curr.next=ListNode(1)
        return head