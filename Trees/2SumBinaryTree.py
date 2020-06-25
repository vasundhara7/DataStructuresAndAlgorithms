# Given a binary search tree T, where each node contains a positive integer, and an integer K, you have to find whether or not there exist two different nodes A and B such that A.value + B.value = K.

# Return 1 to denote that two such nodes exist. Return 0, otherwise.

# Notes

# Your solution should run in linear time and not take memory more than O(height of T).
# Assume all values in BST are distinct.
# Example :

# Input 1: 

# T :       10
#          / \
#         9   20

# K = 19

# Return: 1

# Input 2: 

# T:        10
#          / \
#         9   20

# K = 40

# Return: 0

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
    def t2Sum(self, A, B):
        if A==None:
            return 0
        arr={}
        self.inorder(A,arr)
        for i in arr:
            if B-i in arr and B-i!=i:
                return 1
        return 0
        
    def inorder(self,root,arr):
        if root==None:
            return
        self.inorder(root.left,arr)
        arr[root.val]=1
        self.inorder(root.right,arr)
