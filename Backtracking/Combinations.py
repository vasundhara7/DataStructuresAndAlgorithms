# Given two integers n and k, return all possible combinations of k numbers out of 1 2 3 ... n.

# Make sure the combinations are sorted.

# To elaborate,

# Within every entry, elements should be sorted. [1, 4] is a valid entry while [4, 1] is not.
# Entries should be sorted within themselves.
# Example :
# If n = 4 and k = 2, a solution is:

# [
#   [1,2],
#   [1,3],
#   [1,4],
#   [2,3],
#   [2,4],
#   [3,4],
# ]

class Solution:
    # @param A : integer
    # @param B : integer
    # @return a list of list of integers
    def combine(self, A, B):
        res=[]
        self.findComb(A,1,B,[],res)
        return res
    def findComb(self,n,index,k,r,res):
        if k==0:
            a=r.copy()
            res.append(a)
            return
        if k<0:
            return
        
        for i in range(index,n+1):
            r.append(i)
            self.findComb(n,i+1,k-1,r,res)
            r.pop()
            
            
