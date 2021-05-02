#KCM travel
import sys,math,heapq
test = int(sys.stdin.readline())
for _ in range(test):
    N, K, M = map(int,sys.stdin.readline().split())
    A=[[] for _ in range(N+1)]
    for _ in range(M):
        a,b,c,d = map(int,sys.stdin.readline().split())
        A[a].append([b,c,d])

    dp = [[math.inf for _ in range(K+1)]  for _ in range(N+1)]
    dp[1][0] = 0
    
    ans = math.inf

    for point in range(K+1):
        for cur in range(1,N+1):
            pay = dp[cur][point]
            if pay == math.inf: continue
            if cur == N and ans > pay:
                ans = pay
            for b,c,d in A[cur]:
                if point + c > K or ans < pay+d: continue
                dp[b][point+c] = min(dp[b][point+c],pay+d)

    if ans == math.inf:
        print("Poor KCM")
    else:
        print(ans)
