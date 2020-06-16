def findSubArray(arr):
    if len(arr)==0:
        return 0
    ans=arr[0]
    max_until_here=arr[0]
    for i in range(1,len(arr)):
        max_until_here=max(arr[i],arr[i]+max_until_here)
        ans=max(ans,max_until_here)
    return ans

arr=[int(x) for x in input().split()]
result=findSubArray(arr)
print(result)
