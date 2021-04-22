#회의실배정
import sys 
N = int(sys.stdin.readline())
A = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
A.sort(key=lambda x: (x[1],x[0]))
ans = 0
t = 0
for i in range(N):
    if A[i][0] < t: continue
    ans+=1
    t = A[i][1]
print(ans)