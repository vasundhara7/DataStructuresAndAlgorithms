# Given a binary tree and a sum, find all root-to-leaf paths where each path’s sum equals the given sum.

# For example:
# Given the below binary tree and sum = 22,

#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
# return

# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of list of integers
    def pathSum(self, A, B):
        if not A:
            return []
        paths=[]
        
        self.findPaths(A,B,[],paths)
        return paths
        
    def findPaths(self,root,s,r,paths):
        if root==None:
            return
        r.append(root.val)
        if root.val-s==0 and not root.left and not root.right:
            a=r[:]
            paths.append(r)
           
            return
        self.findPaths(root.left,s-root.val,r[:],paths)
        self.findPaths(root.right,s-root.val,r[:],paths)
        
