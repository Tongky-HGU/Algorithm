#ACM craft
import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N, K = map(int,sys.stdin.readline().split())
    D = [0] + list(map(int,sys.stdin.readline().split()))
    A = [[] for _ in range(N+1)]
    B = [[] for _ in range(N+1)]

    degree = [0 for _ in range(N+1)]
    need = [0 for _ in range(N+1)]

    for _ in range(K):
        a, b = map(int,sys.stdin.readline().split())
        A[a].append(b)
        B[b].append(a)

        degree[b] += 1
    
    W = int(sys.stdin.readline())
    queue = []
    queue.append(W)
    while(queue):
        cur = queue.pop()
        need[cur] = 1
        for i in B[cur]:
            queue.append(i)

    # print(A)
    # print(degree)
    # print(need)

    ans = 0

    while(1):
        time = 0
        queue = []
        for i in range(N+1):
            if degree[i] == 0:
                if need[i] == 1:
                    queue.append(i)
                    time = max(time,D[i])
                degree[i] = -1
            
        ans += time

        if queue:
            for i in queue:
                for j in A[i]:
                    degree[j] -= 1
        else:
            break


    print(ans)
                    

    