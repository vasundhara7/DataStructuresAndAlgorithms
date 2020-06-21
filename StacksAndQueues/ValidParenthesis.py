# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

# Return 0 / 1 ( 0 for false, 1 for true ) for this problem

class Solution:
	# @param A : string
	# @return an integer
	def isValid(self, A):
	    
	    li=[]
	    for i in range(len(A)):
	        
	        if A[i]=='{' or A[i]=='(' or A[i]=='[':
	            
	            li.append(A[i])
	        elif A[i]==')'or A[i]=='}' or A[i]==']':
	            
	            if len(li)==0:
	                
	                return 0
	            else:
	                
                    x=li.pop()
                    if x=='(' and A[i]==')':
                        
                        continue
                    elif x=='{' and A[i]=='}':
                        continue
                    elif x=='[' and A[i]==']':
                        continue
                    else:
                        return 0
	    if len(li)==0:
	        return 1
	    else:
	        return 0
