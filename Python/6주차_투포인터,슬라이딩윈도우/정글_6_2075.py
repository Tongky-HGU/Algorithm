#N번째 큰 수
import sys
import heapq
import math
N = int(sys.stdin.readline())

def solve():
    A = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
    # print(A)

    # window = [0 for _ in range(N)] 
    window = []
    mini = -math.inf;

    for i in range(N):
        for j in range(N):
            if A[i][j] > mini:
                heapq.heappush(window,A[i][j])
                if len(window)==N:
                    mini = heapq.heappop(window)

    # print(window)
    print(mini)

solve()