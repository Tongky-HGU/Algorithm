#부분수열의합2
import sys
from itertools import combinations

N, S = map(int,sys.stdin.readline().split())
A = list(map(int,sys.stdin.readline().split()))

# print(A)

mid = N//2
L = []
R = []
for i in range(mid+1):
    combis = combinations(A[:mid], i)
    for combi in combis:
        L.append(sum(combi))

for i in range(N-mid+1):
    combis = combinations(A[mid:], i)
    for combi in combis:
        R.append(sum(combi))

L.sort(reverse=True)
R.sort()

# print(L,R)

ans = 0
cl = 0
cr = 0
while(cl<len(L) and cr < len(R)):
    temp = L[cl] + R[cr]
    if temp == S:
        L_cnt, R_cnt = 1,1
        L_cur, R_cur = cl,cr
        while(L_cur + 1 < len(L) and L[L_cur]==L[L_cur+1]):
            L_cnt += 1
            L_cur += 1
        while(R_cur + 1 < len(R) and R[R_cur]==R[R_cur+1]):
            R_cnt += 1
            R_cur += 1
        ans += L_cnt * R_cnt
        cl = L_cur + 1
        cr = R_cur + 1

    elif temp < S:
        cr += 1
    else:
        cl += 1 

if ans > 0 and S == 0:
    ans -= 1

print(ans)