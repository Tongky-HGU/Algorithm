#정수삼각형
def solution(triangle):
    dp = [0 for _ in range(len(triangle[-1])+2)]

    for a in triangle:
        temp = [0 for _ in range(len(triangle[-1])+2)]
        for i in range(1,len(a)+1):
            temp[i] = max(dp[i-1],dp[i]) + a[i-1]
        dp = temp

    return max(dp)

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))