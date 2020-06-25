# Given a 2D board and a word, find if the word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The cell itself does not count as an adjacent cell.
# The same letter cell may be used more than once.

# Example :

# Given board =

# [
#   ["ABCE"],
#   ["SFCS"],
#   ["ADEE"]
# ]
# word = "ABCCED", -> returns 1,
# word = "SEE", -> returns 1,
# word = "ABCB", -> returns 1,
# word = "ABFSAB" -> returns 1
# word = "ABCD" -> returns 0

class Solution:
    # @param A : list of strings
    # @param B : string
    # @return an integer
    def exist(self, A, B):
        for i in range(len(A)):
            for j in range(len(A[i])):
                if A[i][j]==B[0] and self.dfs(A,i,j,0,B):
                    return 1
        
        return 0
    
    def dfs(self,board,i,j,index,word):
        if index==len(word):
            return 1
        
        if i<0 or i>=len(board) or j<0 or j>=len(board[i]) or board[i][j]!=word[index]:
            return 0
        found=self.dfs(board,i+1,j,index+1,word) or self.dfs(board,i-1,j,index+1,word) or self.dfs(board,i,j-1,index+1,word) or self.dfs(board,i,j+1,index+1,word)
        
        return found
      