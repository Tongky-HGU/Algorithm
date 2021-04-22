# LCS
import sys 
s1 = str(sys.stdin.readline().rstrip())
s2 = str(sys.stdin.readline().rstrip())

def max_lcs():
	N = len(s1)
	M = len(s2)

	lcs = [[0 for _ in range(M+1)] for _ in range(N+1)]

	for i in range(1,N+1):
		for j in range(1,M+1):
			if s1[i-1] == s2[j-1]:
				lcs[i][j] = lcs[i-1][j-1] + 1
			else:
				lcs[i][j] = max(lcs[i-1][j],lcs[i][j-1])
	print(lcs[-1][-1])

max_lcs()