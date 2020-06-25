# Given N x M character matrix A of O's and X's, where O = white, X = black.

# Return the number of black shapes. A black shape consists of one or more adjacent X's (diagonals not included)

class Solution:
    # @param A : list of strings
    # @return an integer
    def black(self, A):
        count=0
        ans=[]
        for i in range(len(A)):
            li=[]
            for j in range(len(A[i])):
                li.append(A[i][j])
            ans.append(li)
        
        for i in range(len(A)):
            for j in range(len(A[i])):
                if A[i][j]=='X':
                   
                    count+=self.dfs(ans,i,j)
        return count
    
    def dfs(self,arr,i,j):
        
        if i<0 or i>=len(arr) or j<0 or j>=len(arr[i]) or arr[i][j]!='X':
            return 0
        
        arr[i][j]='O'
        self.dfs(arr,i+1,j)
        self.dfs(arr,i-1,j)
        self.dfs(arr,i,j+1)
        self.dfs(arr,i,j-1)
        return 1
        
   
