import math

def solution(a):
    ans = 0
    result = [0 for _ in range(len(a))]
    L , R = math.inf, math.inf
    for i in range(len(a)):
        if a[i] < L:
            L = a[i]
            result[i] = 1
        if a[-1-i] < R:
            R = a[-1-i]
            result[-1-i] = 1
    for i in result:
        if i: ans += 1     

    return ans

print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))