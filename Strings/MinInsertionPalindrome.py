def mininsertion(s,l,h):
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


s=input()
res=mininsertion(s,0,len(s)-1)
print(res)