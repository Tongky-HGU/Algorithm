# 괄호
import sys
n = int(sys.stdin.readline())

def VPS():
    stack =[]
    chk = 0
    for i in range(len(a)):
        if a[i] == '(':
            stack.append(chk)
            chk += 1
        else:
            if chk > 0 and stack[len(stack)-1] == chk-1:
                stack.pop()
                chk -= 1
            else:
                return False
    return chk == 0

for i in range(n):
    a = str(sys.stdin.readline().rstrip())
    result = "YES" if VPS() else "NO"
    print(result)