import sys

N, S, R = map(int, sys.stdin.readline().split())
A = [1 for i in range(N+1)]

no = list(map(int, sys.stdin.readline().split()))
for i in no:
    A[i] -= 1

extra = list(map(int, sys.stdin.readline().split()))
for i in extra:
    A[i] += 1

stack = []
for i in A:
    if i == 1:
        stack.append(i)
    elif i == 0:
        if stack[-1] == 2:
            stack.append(1)
        else:
            stack.append(0)
    elif i == 2:
        if stack[-1] == 0:
            stack[-1] = 1
            stack.append(1)
        else:
            stack.append(2)

print(len(list(filter(lambda x: x == 0, stack))))
