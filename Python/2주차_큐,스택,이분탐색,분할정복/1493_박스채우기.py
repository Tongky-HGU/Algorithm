#박스채우기
import sys
L,W,H = map(int,sys.stdin.readline().split())
N = int(sys.stdin.readline())
A = [0 for _ in range(N)]
for _ in range(N):
    a,b = map(int,sys.stdin.readline().split())
    A[a] = b

cnt = 0
ans = 0
for i in range(N-1,-1,-1):
    cnt <<= 3
    t = min(A[i], (L>>i)*(W>>i)*(H>>i) - cnt)
    cnt += t 
    ans += t

if cnt == L*W*H:
    print(ans)
else:
    print(-1)