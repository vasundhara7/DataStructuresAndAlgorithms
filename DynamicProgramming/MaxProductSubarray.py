# Find the contiguous subarray within an array (containing at least one number) which has the largest product.
# Return an integer corresponding to the maximum product possible.

# Example :

# Input : [2, 3, -2, 4]
# Return : 6 

# Possible with [2, 3]

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProduct(self, A):
        if len(A)==1:
            return A[0]
        max_product=A[0]
        max_val=A[0]
        min_val=A[0]
        for i in range(1,len(A)):
            if A[i]<0:
                temp=min_val
                min_val=max_val
                max_val=temp
            max_val=max(max_val*A[i],A[i])
            min_val=min(min_val*A[i],A[i])
            max_product=max(max_product,max_val)
        return max_product
