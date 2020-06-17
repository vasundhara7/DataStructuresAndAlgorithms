def longestSubsequence(li,n):
    dp=[1]*n
    for j in range(1,n):
        for i in range(0,j):
            if li[j]>li[i]:
                dp[j]=max(dp[j],dp[i]+1)
    return max(dp)
        
            



test=int(input())
for i in range(test):
    n=int(input())
    li=[int(x) for x in input().split()]
    res=longestSubsequence(li,n)
    print(res)
    