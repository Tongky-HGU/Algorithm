# 제로
import sys 
n = int(sys.stdin.readline())
a=[]
for i in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        a.pop()
    else:
        a.append(x)

print(sum(a))
