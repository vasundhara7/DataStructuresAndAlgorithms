def findSubstring(s):
    max_len=0
    ans=0
    d=dict()
    i=0
    while i<len(s):
        if s[i] not in d:
            d[s[i]]=i 
            max_len+=1
            ans=max(ans,max_len)
            i+=1
        else:
            i=d[s[i]]+1
            d=dict()
            max_len=0    
    return ans

s=input()
ans=findSubstring(s)
print("Max length substring without repeating chars= ",ans)

