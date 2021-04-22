#문자열폭팔
import sys
A = str(sys.stdin.readline().rstrip())
B = str(sys.stdin.readline().rstrip())
N = len(B)
last_char = B[-1]
stack =[]
for char in A:
    stack.append(char)
    if char == last_char and "".join(stack[-N:]) == B:
        del stack[-N:]

ans = ''.join(stack)

if ans == "":
    print("FRULA")
else:
    print(ans)