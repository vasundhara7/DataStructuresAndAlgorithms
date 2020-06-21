# Given an array of integers A. There is a sliding window of size B which
# is moving from the very left of the array to the very right.
# You can only see the w numbers in the window. Each time the sliding window moves
# rightwards by one position. You have to find the maximum for each window.
# The following example will give you more clarity.

# The array A is [1 3 -1 -3 5 3 6 7], and B is 3.

# Window position	Max
# ———————————-	————————-
# [1 3 -1] -3 5 3 6 7	3
# 1 [3 -1 -3] 5 3 6 7	3
# 1 3 [-1 -3 5] 3 6 7	5
# 1 3 -1 [-3 5 3] 6 7	5
# 1 3 -1 -3 [5 3 6] 7	6
# 1 3 -1 -3 5 [3 6 7]	7
# Return an array C, where C[i] is the maximum value of from A[i] to A[i+B-1].

# Note: If B > length of the array, return 1 element with the max of the array.

from collections import deque
class Solution:
    # @param arr : tuple of integers
    # @param k: integer
    # @return a list of integers
    def slidingMaximum(self, arr, k):
        if k>=len(arr):
            return [max(arr)]
        q=deque()
        n=len(arr)
        li=[]
        for i in range(k):
            while q and arr[i]>=arr[q[-1]]:
                q.pop()
            q.append(i)
            
        for i in range(k,n):
            
            li.append(arr[q[0]])
            while q and q[0]<=i-k:
                q.popleft()
            while q and arr[i]>=arr[q[-1]]:
                q.pop()
            q.append(i)
        li.append(arr[q[0]])
        return li