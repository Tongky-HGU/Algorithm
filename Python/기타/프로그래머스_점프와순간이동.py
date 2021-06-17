#점프와 순간이동
def solution(n):
    ans = 0
    while(1):
        if n == 0: break
        if n % 2 == 1:
            n = n -1
            ans+=1    
        else:
            n = n//2
    return ans

print(solution(5000))