# Problem Description
# Say you have an array, A, for which the ith element is the price of a given stock on day i.
# If you were only permitted to complete at most one transaction (i.e, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

# Return the maximum possible profit.

# Problem Constraints
# 0 <= len(A) <= 7e5

# 1 <= A[i] <= 1e7

# Input Format
# The first and the only argument is an array of integers, A.

# Output Format
# Return an integer, representing the maximum possible profit.


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        maxi=0
        mini=1000000000000
        for i in range(len(A)):
            if A[i]<mini:
                mini=A[i]
            else:
                maxi=max(maxi,A[i]-mini)
        return maxi
