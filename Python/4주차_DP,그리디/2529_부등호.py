#부등호
import sys 

N = int(sys.stdin.readline())
A = list(sys.stdin.readline().split())
vis = [0 for _ in range(10)]

high, low = "",""

def cmp(i,j,k):
    if k == '<':
        return i<j
    else:
        return i>j

def dfs(cnt,a):
    global high,low
    if cnt == N+1:
        if not len(low):
            low = a
        else:
            high = a
        return
    for i in range(10):
        if not vis[i]:
            if cnt == 0 or cmp(a[-1],str(i),A[cnt-1]):
                vis[i] = 1
                dfs(cnt+1,a+str(i))
                vis[i] = 0

dfs(0,"")
print(high)
print(low)
