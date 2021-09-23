import sys

R, B = map(int,sys.stdin.readline().split())
A = R+B
for i in range(1,A//2):
    j = A/i
    if j % 1 > 0: continue
    if 2*i+2*j-4 == R:
        print(int(j),i)
        break