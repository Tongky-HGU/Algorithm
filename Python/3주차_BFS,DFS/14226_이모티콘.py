#이모티콘
import sys, math
from collections import deque

N = int(sys.stdin.readline())

dp = [[math.inf for _ in range(N+2)] for _ in range(N+2)]

queue = deque()
queue.append([1,0])
dp[1][0]=0

while(queue):
    cur,cpy = queue.popleft()
    # print(f"{cur} {cnt}")
    if dp[cur][cur] == math.inf:
        dp[cur][cur] = dp[cur][cpy] +1
        queue.append([cur,cur])

    if cur+cpy <= N and dp[cur+cpy][cpy] == math.inf:
        dp[cur+cpy][cpy] = dp[cur][cpy] + 1
        queue.append([cur+cpy,cpy])

    if cur-1 >= 1 and dp[cur-1][cpy] == math.inf:
        dp[cur-1][cpy] = dp[cur][cpy] + 1
        queue.append([cur-1,cpy])
    
# print(dp)
print(min(dp[N]))


