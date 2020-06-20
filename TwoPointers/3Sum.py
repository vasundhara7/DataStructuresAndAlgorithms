# Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target.
# Return the sum of the three integers.

# Assume that there will only be one solution

# Example:
# given array S = {-1 2 1 -4},
# and target = 1.

# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2)

import sys
class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return an integer
	def threeSumClosest(self, A, B):
	    if len(A)<3:
            return sys.maxsize
        if len(A)==3:
            return sum(A)
        n=len(A)-1
        A.sort()
        closest_sum=sys.maxsize
        for i in range(len(A)-1):
            j=i+1
            k=n
            while j<k:
                s=A[i]+A[j]+A[k]
                if s==B:
                    return B
                if abs(closest_sum-B)>abs(s-B):
                    closest_sum=s
                if s>B:
                    k-=1
                elif s<B:
                    j+=1
        return closest_sum