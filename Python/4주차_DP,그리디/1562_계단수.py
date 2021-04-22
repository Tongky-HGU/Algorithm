#계단수
import sys
N = int(sys.stdin.readline())
dp =[[[-1 for _ in range(1<<10)] for _ in range(10)] for _ in range (N+1)]

def dfs(level, num, visited):
    # print(f"{level} {num} {visited}")
    if num < 0 or num > 9:
        return 0
    
    if level == N:
        if visited == (1 << 10) -1:
            return 1
        else:
            return 0
    
    if dp[level][num][visited] != -1:
        return dp[level][num][visited] 
    
    ret = 0
    if num == 0:
        ret += dfs(level+1, num+1, visited | 1<<(num+1))
    elif num ==9:
        ret += dfs(level+1, num-1, visited | 1<<(num-1))
    else:
        ret += dfs(level+1, num+1, visited | 1<<(num+1))
        ret += dfs(level+1, num-1, visited | 1<<(num-1))

    dp[level][num][visited] = ret
    ret = ret % 10**9
    return ret

ans = 0
for i in range(1,10):
    ans += dfs(1, i, 1 << i)

ans = ans % 10**9
print(ans)

# ans = 0
# for N in range(1,41):
#     dp =[[[-1 for _ in range(1<<10)] for _ in range(10)] for _ in range (N+1)]
#     ans += dfs(0,0,0)
# print(ans)
