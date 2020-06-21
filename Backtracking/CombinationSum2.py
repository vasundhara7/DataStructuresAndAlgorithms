# Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

# Each number in C may only be used once in the combination.

#  Note:
# All numbers (including target) will be positive integers.
# Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
# The solution set must not contain duplicate combinations.
# Example :

# Given candidate set 10,1,2,7,6,1,5 and target 8,

# A solution set is:

# [1, 7]
# [1, 2, 5]
# [2, 6]
# [1, 1, 6]

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def combinationSum(self, A, B):
        A.sort()
        res=[]
        self.findCombinations(A,B,0,[],res)
        return res
    
    def findCombinations(self,arr,target,index,r,res):
        if target==0:
            a=r[:]
            res.append(a)
            return
        if target<0:
            return
        
        for i in range(index,len(arr)):
            if i==index or arr[i]!=arr[i-1]:
                r.append(arr[i])
                self.findCombinations(arr,target-arr[i],i+1,r,res)
                r.pop()
        