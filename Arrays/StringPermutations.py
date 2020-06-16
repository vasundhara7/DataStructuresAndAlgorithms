def generatePermutations(s,l,r):
    if l==r:
        print (''.join(s))
        return
    for i in range(l,r+1):
        
        s[i],s[l]=s[l],s[i]
        generatePermutations(s,l+1,r)
        s[i],s[l]=s[l],s[i]

li=['a','c','b','d']

generatePermutations(li,0,3)
    