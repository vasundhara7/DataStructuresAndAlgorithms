# Say you have an array, A, for which the ith element is the price of a given stock on day i.

# Design an algorithm to find the maximum profit.

# You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

# However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        profit=0
        for i in range(1,len(A)):
            if A[i]>A[i-1]:
                profit+=A[i]-A[i-1]
        return profit
