# Given A, generate all structurally unique BST’s (binary search trees) that store values 1…A.

# Input Format:

# The first and the only argument of input contains the integer, A.
# Output Format:

# Return a list of tree nodes representing the generated BST's.
# Constraints:

# 1 <= A <= 15
# Example:

# Input 1:
#     A = 3

# Output 1:

#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : integer
    # @return a list of TreeNode 
    def generateTrees(self, A):
        
        return self.construct(1,A)
    def construct(self,start,end):
        r=[]
        if start>end:
            r.append(None)
            
            return r
        
        for i in range(start,end+1):
            leftSubtree=self.construct(start,i-1)
            rightSubtree=self.construct(i+1,end)
            
            for j in range(len(leftSubtree)) : 
                left = leftSubtree[j]  
                for k in range(len(rightSubtree)):  
                    right = rightSubtree[k]  
                    node = TreeNode(i)   # making value i as root  
                    node.left = left    # connect left subtree  
                    node.right = right    # connect right subtree  
                    r.append(node)  
                
                # add this tree to list  
        
        return r
    
