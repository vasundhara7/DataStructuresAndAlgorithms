class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s)<=1:
            if len(s)==1 and s[0]=='0':
                return 0
            return 1
        dp=[-1]*len(s)
        
        res=self.decodeWays(s,0,dp)
        return res
        
    def decodeWays(self,s,ptr,dp):
        if  ptr>=len(s):


            return 1
        if dp[ptr]!=-1:
            return dp[ptr]
        res=0
        for i in range(1,3):
            if ptr+i<=len(s):
                sub=s[ptr:ptr+i]
                if self.valid(sub):
                    res+=self.decodeWays(s,ptr+i,dp)
        dp[ptr]=res
            
       
        return dp[ptr]
    
    def valid(self,s):
        if len(s)==0 or s[0]=='0':
            return False
        i=int(s)
        return i>=1 and i<=26