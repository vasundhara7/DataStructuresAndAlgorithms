def generateParenthesis(combination,l,r,n):
    if len(combination)==2*n:
        print(combination)
        return
    if l<n:
        generateParenthesis(combination+'(',l+1,r,n)
    if r<l:
        generateParenthesis(combination+')',l,r+1,n)

n=int(input())
generateParenthesis("",0,0,n)
