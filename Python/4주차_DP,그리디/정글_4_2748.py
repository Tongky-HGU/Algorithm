#피보나치 수2
import sys
N = int(sys.stdin.readline())
ans =[0]+[1]+[0]*N
for i in range(2,N+1):
    ans[i] = ans[i-2] + ans[i-1]

print(ans[N])
