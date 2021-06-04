#후위표기식
import sys
# - dfs 로 풀다가 망함
# stack 사용
A = sys.stdin.readline().rstrip()
stack = []
ans = ""
# is alpha로 구분
for x in A:
    if x.isalpha():
        ans+=x
    else:
        if x == '(':
            stack.append(x)
        elif x == '*' or x == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                ans += stack.pop()
            stack.append(x)
        elif x == '+' or x == '-':
            while stack and stack[-1] != '(':
                ans += stack.pop()
            stack.append(x)
        elif x == ')':
            while stack and stack[-1] != '(':
                ans += stack.pop()
            stack.pop()
    # print(stack, ans)

while stack:
    ans += stack.pop()
print(ans)


