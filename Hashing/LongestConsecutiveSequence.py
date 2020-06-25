# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

# Example:
# Given [100, 4, 200, 1, 3, 2],
# The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

# Your algorithm should run in O(n) complexity.

from collections import Counter
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestConsecutive(self, A):
        if len(A)<=1:
            return len(A)
        d=Counter(A)
        max_count=0
        for i in range(len(A)):
            if A[i]-1 in d:
                continue
            j=A[i]
            count=0
            while j in d:
                count+=1
                j+=1
            max_count=max(max_count,count)
        return max_count
