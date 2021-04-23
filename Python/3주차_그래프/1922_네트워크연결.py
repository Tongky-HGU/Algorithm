#네트워크 연결
import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
vis = [ 0 for _ in range(N+1)]
A = []
ans = 0
cnt = 0

for _ in range(M):
    a,b,c = map(int,sys.stdin.readline().split())
    A.append([c,a,b])
A = sorted(A)

vis[A[0][1]] = 1
cnt += 1
while(cnt < N):
    for i in range(M):
        if vis[A[i][1]] == 1 and vis[A[i][2]] == 0:
            vis[A[i][2]] = 1
            ans += A[i][0]
            cnt +=1
            break
        elif vis[A[i][1]] == 0 and vis[A[i][2]] == 1:
            vis[A[i][1]] = 1
            ans += A[i][0]
            cnt +=1
            break

print(ans)
