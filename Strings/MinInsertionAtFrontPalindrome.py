class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        newstr=A+'$'+A[::-1]
        table=self.getLPS(newstr)
        return len(A)-table[-1]
    
    def getLPS(self,s):
        table=[0]*len(s)
        i=0
        j=1
        while i<len(s) and j<len(s):
            if s[i]==s[j]:
                table[j]=i+1
                i+=1
                j+=1
            else:
                
                if i>0:
                    i=table[i-1]
                else:
                    j+=1
                    
        
        return table
                    