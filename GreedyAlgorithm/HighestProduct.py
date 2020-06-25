# Given an array A, of N integers A.

# Return the highest product possible by multiplying 3 numbers from the array.

# NOTE: Solution will fit in a 32-bit signed integer.



# Input Format:

# The first and the only argument is an integer array A.

# Output Format:

# Return the highest possible product.

class Solution:
    # @param A : list of integers
    # @return an integer
    def maxp3(self, A):
        if len(A)<=2:
            return 0
        A.sort()
        if len(A)==3:
            return A[0]*A[1]*A[2]
        
        if A[0]<0:
            p=A[0]*A[1]
        
        prod=p*A[-1]
        end_p=A[len(A)-1]*A[len(A)-2]*A[len(A)-3]
        return max(prod,end_p)
        
