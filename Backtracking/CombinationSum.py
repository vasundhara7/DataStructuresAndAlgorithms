# Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

# The same repeated number may be chosen from C unlimited number of times.

#  Note:
# All numbers (including target) will be positive integers.
# Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
# The combinations themselves must be sorted in ascending order.
# CombinationA > CombinationB iff (a1 > b1) OR (a1 = b1 AND a2 > b2) OR … (a1 = b1 AND a2 = b2 AND … ai = bi AND ai+1 > bi+1)
# The solution set must not contain duplicate combinations.
# Example,
# Given candidate set 2,3,6,7 and target 7,
# A solution set is:

# [2, 2, 3]
# [7]

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def combinationSum(self, A, B):
        A=list(set(A))
        A.sort()
        res=[]
        r=[]
        self.findnum(A,res,r,B,0)
        return res
    
    def findnum(self,arr,res,r,s,i):
        if s<0:
            return
        if s==0:
            a=r.copy()
            res.append(a)
        
        while i<len(arr) and s-arr[i]>=0:
            r.append(arr[i])
            self.findnum(arr,res,r,s-arr[i],i)
            i+=1
            r.pop()
            
        
