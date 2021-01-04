# 멀티탭 스케줄링
import sys, heapq, math
N, K = map(int,sys.stdin.readline().split())
A = list(map(int,sys.stdin.readline().split()))

cnt = [[] for _ in range(K+1)]
used = [0 for _ in range(K+1)]

for i in range(len(A)):
    cnt[A[i]].append(i)

ans = 0
plug =[]
for i in range(0,K):
    flag = True
    for j in range(len(plug)):
        if plug[j][1] == A[i]:
            del plug[j]
            flag =False
            break
    if flag:
        if len(plug) >= N:
            ans += 1
            heapq.heappop(plug)

    if len(cnt[A[i]])-used[A[i]] > 1:
        heapq.heappush(plug,[-cnt[A[i]][used[A[i]]+1],A[i]])
    else:
        heapq.heappush(plug,[-math.inf,A[i]])
    used[A[i]] +=1
    # print(plug)
# print(used)
print(ans)