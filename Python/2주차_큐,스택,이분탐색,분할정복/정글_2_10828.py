# 스택
import sys

class stack():
    def __init__(self):
        self.a = [0]*10000
        self.len = 0
    
    def push(self,x):
        self.a[self.len]=x
        self.len +=1

    def pop(self):
        if self.len == 0:
            return -1
        else:
            pop = self.a[self.len-1]
            self.len -=1
            return pop

    def size(self):
        return self.len

    def empty(self):
        if self.len == 0:
            return 1
        else:
            return 0

    def top(self):
        if self.len == 0:
            return -1
        else:
            return self.a[self.len-1]

a = stack()

n = int(sys.stdin.readline())
for i in range(n):
    x = list(map(str,sys.stdin.readline().split()))
    if x[0] == "push":
        a.push(int(x[1]))
    elif x[0] == "pop":
        print(a.pop())
    elif x[0] == "size":
        print(a.size())
    elif x[0] == "empty":
        print(a.empty())
    elif x[0] == "top":
        print(a.top())