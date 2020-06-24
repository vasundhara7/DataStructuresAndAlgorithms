# Given a binary tree, return the preorder traversal of its nodes’ values.

# Example :
# Given binary tree

#    1
#     \
#      2
#     /
#    3
# return [1,2,3].

# Using recursion is not allowed.

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def preorderTraversal(self, A):
        if not A:
            return A
        stack=[]
        li=[]
        stack.append(A)
        while len(stack):
            x=stack.pop()
            if x.right:
                stack.append(x.right)
            if x.left:
                stack.append(x.left)
            li.append(x.val)
        return li
