#히든넘버
import sys
N = int(sys.stdin.readline().rstrip())
A = str(sys.stdin.readline().rstrip())
ans = 0
temp = 0

for i in range(N):
    if ord(A[i]) >= 48 and ord(A[i]) <=57:
        temp = temp *10 + int(A[i])
    else:
        ans += temp
        temp = 0
        
ans+=temp

print(ans)