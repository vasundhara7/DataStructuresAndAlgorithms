def climbingStairsRecursive(n):
    if n<=1:
        return 1
    ways=climbingStairsRecursive(n-1)+climbingStairsRecursive(n-2)
    return ways


def climbingStairsDP(n):
    if n==0 or n==1:
        return 1
    dp=[1 for i in range(n+1)]
    for i in range(2,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[-1]

def countWays(n):
    return climbingStairsRecursive(n)

n=int(input())
res=climbingStairsDP(n)
print(res)