#ACM craft
import sys
from collections import deque

T = int(sys.stdin.readline())
for _ in range(T):
    N, K = map(int,sys.stdin.readline().split())
    D = [0] + list(map(int,sys.stdin.readline().split()))
    A = [[] for _ in range(N+1)]
    time = [0 for _ in range(N+1)]

    degree = [0 for _ in range(N+1)]

    for _ in range(K):
        a, b = map(int,sys.stdin.readline().split())
        A[a].append(b)
        degree[b] += 1

    W = int(sys.stdin.readline())

    # print(A)
    # print(degree)
    # print(need)

    queue = deque()
    for i in range(N+1):
        if degree[i] == 0:
            queue.append(i)
            time[i] = D[i]
    while(queue):
        cur = queue.popleft()            
        for j in A[cur]:
            degree[j] -= 1
            time[j] = max(time[cur]+D[j],time[j])
            if degree[j] == 0:
                queue.append(j)
        # print(degree)
        # print(time)
    print(time[W])
                    

    