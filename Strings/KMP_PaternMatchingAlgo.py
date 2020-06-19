def kmp(s,p):
    pattern=[0]*len(p)
    i=0
    j=1 
    while j<len(p) and i<len(p):
        if p[i]==p[j]:
            pattern[j]=i+1 
            i+=1 
            j+=1 
        else:
            if i>0:
                i=pattern[i-1]
            else:
                j+=1
            continue
             
    print(pattern)
    
    i=0
    index=0
    while i<len(s) :
        if s[i]==p[index]:
            i+=1
            index+=1 
        if index==len(p):
            return i-len(p)
        elif i<len(s) and s[i]!=p[index]:
            if index>0:
                index=pattern[index-1]
            else:
                i+=1
    
    if index>=len(p):
        return True
    else:
        return False
        
res=kmp("ABABDABACDABABCABAB","AAACAAAA")
print(res)
            