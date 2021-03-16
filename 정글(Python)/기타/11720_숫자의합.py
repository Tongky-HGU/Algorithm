#숫자의 합
import sys
N = int(sys.stdin.readline())
ans = 0
A = str(sys.stdin.readline().rstrip())
for i in range(len(A)):
    ans += int(A[i])
print(ans)