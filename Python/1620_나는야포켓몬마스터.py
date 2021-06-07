# 나는야 포켓몬 마스터 이다솜
import sys
N,M = map(int,sys.stdin.readline().split())
A = [sys.stdin.readline().rstrip() for _ in range(N)]
Q = [sys.stdin.readline().rstrip() for _ in range(M)]
# set에 넣고 string이면 꺼내오고, 번호면 array로 불러오기

set = {}
for idx,string in enumerate(A):
    set[string] = idx +1

for string in Q:
    if string.isalpha():
        print(set[string])
    else:
        print(A[int(string)-1])