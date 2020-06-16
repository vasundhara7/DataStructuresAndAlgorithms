
def catalanNumber(n):
    if n<=1:
        return 1 
    res=0
    for i in range(n):
        res+=catalanNumber(n-i-1)*catalanNumber(i)
    return res
    


n=int(input())
result=catalanNumber(n)
print("Nth catalan number is ",result)