# 탑
import sys
n = int(sys.stdin.readline())
a= list(map(int,sys.stdin.readline().split()))
stack = []
result = [0]*n

for i in range(n):
    t = a[i]
    while stack and a[stack[-1]] < t :
        stack.pop()
    if stack:
        result[i] = stack[-1] +1
    stack.append(i)

print(*result)
