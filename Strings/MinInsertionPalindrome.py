def mininsertionRecursive(s,l,h):
    if l>h:
        return 100000000
    if l==h:
        return 0 
    if h-l==1:
        if s[l]==s[h]:
            return 0
        else:
            return 1 
    
    if s[l]==s[h]:
        return mininsertion(s,l+1,h-1)
    else:
        return 1+ min(mininsertion(s,l+1,h),mininsertion(s,l,h-1))

def mininsertionDP(s):
    
    dp=[[0 for i in range(len(s))]for j in range(len(s))]

    for gap in range(1,len(s)):
        l=0
        for h in range(gap,len(s)):
            if s[l]==s[h]:
                dp[l][h]=dp[l+1][h-1]
            else:
                dp[l][h]=1+min(dp[l+1][h],dp[l][h-1])
            l+=1
    return dp[0][len(s)-1]



s=input()
res=mininsertionDP(s)
print(res)