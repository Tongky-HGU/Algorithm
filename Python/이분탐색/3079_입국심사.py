import sys
from functools import reduce
N, M = map(int, sys.stdin.readline().split())
A = [int(sys.stdin.readline()) for _ in range(N)]

cl = 0;
cr = max(A)*M

while cl <= cr:
    mid = (cl+cr)//2
    cnt = reduce(lambda p, x: p + mid//x,A,0)
    if cnt >= M:
        cr = mid - 1
    else:
        cl = mid + 1

print(cl)