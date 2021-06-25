# 순위
def solution(n, results):
    ans = 0
    A = [[0 for _ in range(n)]  for _ in range(n)]
    for a,b in results:
        A[a-1][b-1] = 1
        A[b-1][a-1] = -1

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if A[j][k] == 0 :
                    if A[j][i] == 1 and A[i][k] == 1:
                        A[j][k] = 1
                    if A[j][i] == -1 and A[i][k] == -1:
                        A[j][k] = -1

    # print(A)
    for i in range(n):
        cnt = 0
        for j in range(n):
            if A[i][j] != 0: cnt += 1
        if cnt == n-1:
            ans +=1

    return ans

print(solution(5,	[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))