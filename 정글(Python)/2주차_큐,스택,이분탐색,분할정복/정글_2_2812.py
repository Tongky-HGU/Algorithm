# 크게만들기 
import sys

N, K = list(map(int,sys.stdin.readline().split()))
a = list(str(sys.stdin.readline().rstrip()))

def sol():
    stack=[]
    k = 0
    for i in range(len(a)):
        while stack and stack[-1] < int(a[i]):
            if k==K: break
            stack.pop()
            k+=1
        stack.append(int(a[i]))

    for i in range(len(a)-K):
        print(stack[i],end='')
    return stack

sol()
    
    