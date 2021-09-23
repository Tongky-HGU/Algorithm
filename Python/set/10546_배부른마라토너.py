import sys

N = int(sys.stdin.readline())
A = {}

for _ in range(2*N-1):
    name = sys.stdin.readline().rstrip()
    if name in A:
        del A[name]
    else:
        A[name] = True    

for name in A.keys():
    print(name)
