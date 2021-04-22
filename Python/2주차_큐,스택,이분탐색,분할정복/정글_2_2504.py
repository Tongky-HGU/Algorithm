import sys
a = str(sys.stdin.readline().rstrip())
def check():
    stack = []
    temp = 1
    ans = 0
    last = []
    for i in a:
        if i == '(':
            temp *=2
            stack.append(i)

        elif i == '[':
            temp *=3
            stack.append(i)

        elif i == ')':
            temp //= 2
            if last == '[':
                return 0
            elif last == '(':
                ans += temp*2
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                return 0

        elif i == ']':
            temp //= 3
            if last == '(':
                return 0
            elif last == '[':
                ans += temp*3
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                return 0
                
        last = i
    if len(stack) != 0:
        return 0
    return ans

print(check())
            

            
