# Given a 2D integer array A of size M x N, you need to find a path from top left to bottom right which minimizes the sum of all numbers along its path.

# NOTE: You can only move either down or right at any point in time.

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def minPathSum(self, A):
        if len(A)==0:
            return 0
        dp=[[0 for i in range(len(A[0]))]for y in range(len(A))]
        for i in range(len(A)):
            for j in range(len(A[0])):
                dp[i][j]+=A[i][j]
                if i>0 and j>0:
                    dp[i][j]+=min(dp[i-1][j],dp[i][j-1])
                elif i>0:
                    dp[i][j]+=dp[i-1][j]
                elif j>0:
                    dp[i][j]+=dp[i][j-1]
        
        return dp[len(A)-1][len(A[0])-1]
