# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# push(x) – Push element x onto stack.
# pop() – Removes the element on top of the stack.
# top() – Get the top element.
# getMin() – Retrieve the minimum element in the stack.
# Note that all the operations have to be constant time operations.

class MinStack:
    # @param x, an integer
    def __init__(self):
        self.min_li=[]
        self.li=[]
    def push(self, x):
        self.li.append(x)
        if len(self.min_li)==0:
            self.min_li.append(x)
        else:
            self.min_li.append(min(self.min_li[-1],x))


    # @return nothing
    def pop(self):
        if len(self.li)==0:
            pass
        else:
            self.li.pop()
            self.min_li.pop()


    # @return an integer
    def top(self):
        if len(self.li)==0:
            return -1
        return self.li[-1]


    # @return an integer
    def getMin(self):
        if len(self.li)==0:
            return -1
        return self.min_li[-1]

