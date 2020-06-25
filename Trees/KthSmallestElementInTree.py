# Given a binary search tree, write a function to find the kth smallest element in the tree.

# Example :

# Input : 
#   2
#  / \
# 1   3

# and k = 2

# Return : 2

# As 2 is the second smallest element in the tree.
#  NOTE : You may assume 1 <= k <= Total number of nodes in BST 

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, B):
        arr=[]
        self.inorder(A,arr)
        return arr[B-1]
    
    def inorder(self,root,arr):
        if root==None:
            return
        self.inorder(root.left,arr)
        arr.append(root.val)
        self.inorder(root.right,arr)
    
        