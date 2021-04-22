#최종순위
import sys
from collections import deque

test = int(sys.stdin.readline())

for _ in range(test):
    error = False;
    N = int(sys.stdin.readline())
    degree = [i for i in range(N-1,-1,-1)]
    A = list(map(int,sys.stdin.readline().split()))
    M = int(sys.stdin.readline())
    # print(A)
    # print(degree)
    for _ in range(M):
        a,b = map(int,sys.stdin.readline().split())
        a_rank = 0
        b_rank = 0
        for i in range(N):
            if A[i] == a:
                a_rank = i
            elif A[i] == b:
                b_rank = i
        if a_rank > b_rank:
            degree[a_rank] += 1
            degree[b_rank] -= 1
        else:
            degree[a_rank] -= 1
            degree[b_rank] += 1

    # print(degree)
    queue = deque()
    ans = deque()

    for i in range(N):
        if degree[i] == 0:
            queue.append(i) 

    while(queue):
        if len(queue) > 1:
            error = True
            break
        i = queue.pop()
        ans.appendleft(A[i])
        for i in range(N):
            degree[i] -= 1
            if degree[i] == 0:
                queue.append(i) 
    if (error == True):
        print("?")
    elif len(ans) < N:
        print("IMPOSSIBLE")
    else:
        for i in range(N):
            print(ans[i],end=" ")
        print()

