# Given an array of integers A of size N. A represents a histogram i.e A[i] denotes height of
# the ith histogram’s bar. Width of each bar is 1.

# Largest Rectangle in Histogram: Example 1

# Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

# Largest Rectangle in Histogram: Example 2

# The largest rectangle is shown in the shaded area, which has area = 10 unit.

# Find the area of largest rectangle in the histogram.


class Solution:
    # @param A : list of integers
    # @return an integer
    def largestRectangleArea(self, A):
        if len(A)==1:
            return A[0]
        li=[]
        i=0
        max_area=0
        area=0
        while i<len(A):
            if len(li)==0 or A[li[-1]]<=A[i]:
                li.append(i)
                i+=1
            else:
                x=li.pop()
                if len(li):
                    area=A[x]*(i-li[-1]-1)
                else:
                    area=A[x]*i
                max_area=max(max_area,area)
                
        while len(li):
            x=li.pop()
            if len(li):
                    area=A[x]*(i-li[-1]-1)
            else:
                area=A[x]*i
            max_area=max(max_area,area)
        return max_area
