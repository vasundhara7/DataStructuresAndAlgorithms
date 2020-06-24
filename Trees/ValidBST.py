# Given a binary tree, determine if it is a valid binary search tree (BST).

# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node’s key.
# The right subtree of a node contains only nodes with keys greater than the node’s key.
# Both the left and right subtrees must also be binary search trees.
# Example :

# Input : 
#    1
#   /  \
#  2    3

# Output : 0 or False


# Input : 
#   2
#  / \
# 1   3

# Output : 1 or True 
# Return 0 / 1 ( 0 for false, 1 for true ) for this problem


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys
class Solution:
    # @param A : root node of tree
    # @return an integer
    def isValidBST(self, A):
        if not A:
            return 1
        return self.check(A,None,None)
    
    def check(self,root,mini,maxi):
        if root==None:
            return 1
        if (min!=None and root.val<=mini) or (maxi!=None and root.val>=maxi):
            return 0
        elif (not self.check(root.left,mini,root.val) or not self.check(root.right,root.val,maxi)):
            return 0
        else:
            return 1