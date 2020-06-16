test=int(input())
for t in range(test):
    m=int(input())
    coins=[int(x) for x in input().split()]
    coins.sort()
    n=int(input())
    matrix=[[0 for x in range(n+1)] for y in range(m+1)]
    for i in range(m+1):
        matrix[i][0]=1
    
    for i in range(1,m+1):
        for j in range(1,n+1):
            if j-coins[i-1]>=0:
                matrix[i][j]=matrix[i-1][j]+matrix[i][j-coins[i-1]]
                
            else:
                matrix[i][j]=matrix[i-1][j]
    
    print(matrix[i][j])