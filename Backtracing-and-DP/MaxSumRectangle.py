def findMaxSum(arr,rows,cols):
    sum_arr=[0]*rows
    max_sum=arr[0][0]
   
    for l in range(cols):
        sum_arr=[0]*rows
        for r in range(l,cols):
            for i in range(rows):
                sum_arr[i]+=arr[i][r]
            # print("running sum=",sum_arr)
            max_here=kadane(sum_arr)
            # print("kadane max_sum",max_here)
            max_sum=max(max_sum,max_here)
            # print("max now",max_sum)
    return max_sum
            
        
def kadane(arr):
    max_until=arr[0]
    max_sum=arr[0]
    for i in range(1,len(arr)):
        max_until=max(arr[i],max_until+arr[i])
        max_sum=max(max_sum,max_until)
    return max_sum

# rows=int(input())
# cols=int(input())
# matrix=[]
# for i in range(rows):
#     matrix.append([int(x) for x in input().split()])
    
m=[[1, 2, -1, -4, 20], 
	[-8, -3, 4, 2, 1], 
	[3, 8, 10, 1, 3], 
	[-4, -1, 1, 7, 6]] 
res=findMaxSum(m,4,5)
print(res)
