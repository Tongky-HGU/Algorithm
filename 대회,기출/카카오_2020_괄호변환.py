def divide(a):
    left = 0
    right = 0
    for idx,char in enumerate(a):
        if char == '(':
            left += 1
        else:
            right += 1
        if left == right:
            return a[0:idx+1], a[idx+1:]
        
def check(a):
    stack = []
    for char in a:
        if char == ')':
            if not stack: return False
            last = stack.pop()
            if last == ')': return False
        else:
            stack.append(char)
    return True

def solution(p):
    ans = ''

    #1 
    if not p:
        return ans
    
    #2 
    u,v = divide(p)
    # print(u,v)
        
    #3
    if check(u):
        return u + solution(v)
    
    #4
    ans = '(' + solution(v) + ')'
    for char in u[1:-1]:
        if char == '(':
            ans += ')'
        else:
            ans += '('
    # print(ans)    
    return ans
