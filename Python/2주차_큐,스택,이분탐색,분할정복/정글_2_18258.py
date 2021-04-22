# 큐2
import sys
n = int(sys.stdin.readline().rstrip())

class queue():
    def __init__(self,n):
        self.a = [0]*n
        self.ptr = 0
        self.valid = 0

    def push(self,x):
        self.a[self.ptr] = x
        self.ptr +=1
    
    def pop(self):
        if (self.ptr - self.valid) == 0:
            print(-1)
        else:
            print(self.a[self.valid])
            self.valid +=1

    def size(self):
        print(self.ptr-self.valid)
    
    def empty(self):
        if (self.ptr - self.valid) == 0:
            print(1)
        else: 
            print(0)
    
    def front(self):
        if (self.ptr - self.valid) == 0:
            print(-1)
        else:
            print(self.a[self.valid])

    def back(self):
        if (self.ptr - self.valid) == 0:
            print(-1)
        else:
            print(self.a[self.ptr-1])


myqueue = queue(n)

for i in range(n):
    x = list(map(str,sys.stdin.readline().rstrip().split()))
    if x[0] == "push":
        myqueue.push(int(x[1]))
    elif x[0] == "pop":
        myqueue.pop()
    elif x[0] == "size":
        myqueue.size()
    elif x[0] == "empty":
        myqueue.empty()
    elif x[0] == "front":
        myqueue.front()
    elif x[0] == "back":
        myqueue.back()