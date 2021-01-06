#01타일
import sys

dp = [[[0 for _ in range(21)]for _ in range(21)] for _ in range(21)]

def w(a,b,c):
	if a<= 0 or b <= 0 or c <= 0:
		return 1
	elif a > 20 or b > 20 or c > 20:
		return w(20, 20, 20)

	if dp[a][b][c]:
		return dp[a][b][c]

	if a < b < c : 
		dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
	else:
		dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
	return dp[a][b][c]

while(1):
	A,B,C = map(int,sys.stdin.readline().split())
	if A == -1 and B == -1 and C ==-1:
		break
	print(f"w({A}, {B}, {C}) = {w(A,B,C)}")
