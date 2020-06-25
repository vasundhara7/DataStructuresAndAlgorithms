# There are N children standing in a line. Each child is assigned a rating value.

# You are giving candies to these children subjected to the following requirements:

# 1. Each child must have at least one candy.
# 2. Children with a higher rating get more candies than their neighbors.
# What is the minimum candies you must give?

# Input Format:

# The first and the only argument contains N integers in an array A.
# Output Format:

# Return an integer, representing the minimum candies to be given.

class Solution:
    # @param A : list of integers
    # @return an integer
    def candy(self, A):
        left=[1]*len(A)
        right=[1]*len(A)
        
        for i in range(1,len(A)):
            if A[i]>A[i-1]:
                left[i]=left[i-1]+1
        
        for i in range(len(A)-2,-1,-1):
            if A[i]>A[i+1]:
                right[i]=right[i+1]+1
        s=0
        for i in range(len(left)):
            s+=max(left[i],right[i])
        return s