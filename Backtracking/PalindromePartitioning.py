# Given a string s, partition s such that every string of the partition is a palindrome.

# Return all possible palindrome partitioning of s.

# For example, given s = "aab",
# Return

#   [
#     ["a","a","b"]
#     ["aa","b"],
#   ]
#  Ordering the results in the answer : Entry i will come before Entry j if :
# len(Entryi[0]) < len(Entryj[0]) OR
# (len(Entryi[0]) == len(Entryj[0]) AND len(Entryi[1]) < len(Entryj[1])) OR
# *
# *
# *
# (len(Entryi[0]) == len(Entryj[0]) AND … len(Entryi[k] < len(Entryj[k]))
# In the given example,
# ["a", "a", "b"] comes before ["aa", "b"] because len("a") < len("aa")

class Solution:
    # @param A : string
    # @return a list of list of strings
    def partition(self, A):
        res=[]
        self.findPalindrome(A,0,[],res)
        return res
    
    def findPalindrome(self,s,ptr,r,res):
        if ptr==len(s):
            a=r[:]
            res.append(a)
            return
        else:
            for i in range(ptr,len(s)):
                if self.isPalindrome(s,ptr,i):
                    sub=s[ptr:i+1]
                    r.append(sub)
                    self.findPalindrome(s,i+1,r,res)
                    r.pop()
    def isPalindrome(self,string,low,high):
        while low < high: 
            if string[low] != string[high]: 
                return False
            low += 1
            high -= 1
        return True
