#에디터
import sys
A = list(sys.stdin.readline().rstrip())
B = []

N = int(sys.stdin.readline())

for _ in range(N):
    C = list(sys.stdin.readline().rstrip().split())
    if C[0]=="P":
        A.append(C[1])
    elif C[0] == "L":
        if A:
            B.append(A.pop())
    elif C[0] == "D":
        if B:
            A.append(B.pop())
    elif C[0] == "B":
        if A:
            A.pop()

print("".join(A+list(reversed(B))))