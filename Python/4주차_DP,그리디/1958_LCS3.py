#LCS3
import sys
A = str(sys.stdin.readline().rstrip())
B = str(sys.stdin.readline().rstrip())
C = str(sys.stdin.readline().rstrip())
dp = [[[ 0 for _ in range(len(A)+1)] for _ in range(len(B)+1)] for _ in range((len(C)+1))]
for i in range(1,len(A)+1):
    for j in range(1,len(B)+1):
        for k in range(1,len(C)+1):
            # print(f"{A[i-1]} {B[j-1]} {C[k-1]}")
            # print("why")
            if A[i-1] == B[j-1] == C[k-1]:
                dp[k][j][i] = dp[k-1][j-1][i-1]+1
            else:
                dp[k][j][i] = max(dp[k-1][j][i],dp[k][j-1][i],dp[k][j][i-1])

# print(dp)
print(dp[k][j][i])



