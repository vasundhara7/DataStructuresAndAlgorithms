# Given a collection of integers that might contain duplicates, S, return all possible subsets.

#  Note:
# Elements in a subset must be in non-descending order.
# The solution set must not contain duplicate subsets.
# The subsets must be sorted lexicographically.
# Example :
# If S = [1,2,2], the solution is:

# [
# [],
# [1],
# [1,2],
# [1,2,2],
# [2],
# [2, 2]
# ]

class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsetsWithDup(self, A):
        res=[]
        A.sort()
        self.findSubsets(A,0,[],res)
        return res
        
    def findSubsets(self,arr,index,r,res):
        a=r.copy()
        res.append(a)
        for i in range(index,len(arr)):
            if i==index or arr[i]!=arr[i-1]:
                r.append(arr[i])
                self.findSubsets(arr,i+1,r,res)
                r.pop()
