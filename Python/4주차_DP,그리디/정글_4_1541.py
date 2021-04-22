# 잃어버린괄호
import sys
A = str(sys.stdin.readline().rstrip())
num=0
ans = 0
flag = 1
for i in range(len(A)):
    if A[i] == '+':
        ans += num *flag
        num = 0

    elif A[i] == '-':
        ans += num *flag
        flag = -1
        num = 0
    else:
        num = num*10 + int(A[i])
ans += num *flag
print(ans)
