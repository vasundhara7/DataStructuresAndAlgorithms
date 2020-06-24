# Given two binary trees, write a function to check if they are equal or not.

# Two binary trees are considered equal if they are structurally identical and the nodes have the same value.

# Return 0 / 1 ( 0 for false, 1 for true ) for this problem

# Example :

# Input : 

#    1       1
#   / \     / \
#  2   3   2   3

# Output : 
#   1 or True

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : root node of tree
    # @return an integer
    def isSameTree(self, A, B):
        if not A and not B:
            return 1
        if not A or not B:
            return 0
        if A.val==B.val:
            return self.isSameTree(A.left,B.left) and self.isSameTree(A.right,B.right)
        else:
            return 0
