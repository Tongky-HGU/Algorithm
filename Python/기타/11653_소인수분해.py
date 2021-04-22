#소인수분해
import sys
N = int(sys.stdin.readline())
i = 2

while i <= N:
    if (N % i) == 0:
        print(i)
        N = N//i
    else:
        i+=1