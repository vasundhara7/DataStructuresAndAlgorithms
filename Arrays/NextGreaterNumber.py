def nextPermutation(arr):
    i=len(arr)-2
    while i>=0:
        if arr[i]<arr[i+1]:
            break
        i-=1
    if i==-1:
        return []
    minindex=i+1
    minval=arr[i+1]
    for j in range(i+1,len(arr)):
        if arr[j]>arr[i] and arr[j]<minval:
            minval=arr[j]
            minindex=j
    
    arr[i],arr[minindex]=arr[minindex],arr[i]
    arr=arr[0:i+1]+arr[len(arr):i:-1]
    return arr

arr=[int(x) for x in input().split()]
res=nextPermutation(arr)
print(res)

    