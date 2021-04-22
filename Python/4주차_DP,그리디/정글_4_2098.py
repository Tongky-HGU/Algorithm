#외판원순회
import sys, math
N = int(sys.stdin.readline())
A = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
dp = [[None]*(1<<N) for _ in range(N)]

def dfs(last,visited):
    if visited == (1<<N)-1:
        return A[last][0] or math.inf

    if dp[last][visited] != None:
        return dp[last][visited]
    
    tmp = math.inf

    for i in range(N):
        if visited & (1<<i) == 0 and A[last][i] != 0:
            tmp = min(tmp,dfs(i,visited | (1<<i))+A[last][i])
    dp[last][visited] = tmp
    return tmp

print(dfs(0,1<<0))


            
