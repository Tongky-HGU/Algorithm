# 차이를 최대로

def cal(a):
    ans = 0
    for i in range(n-1):
        ans += abs(a[i]- a[i+1])
    return ans

def set(i):
    global max_ans
    for j in range(n):
        if not f[j]:
            b[i] = a[j]
            if i == n-1:
                # print(b)
                if cal(b) > max_ans:
                    max_ans = cal(b)
            else:
                f[j]=True
                set(i+1)
                f[j]=False


n = int(input())
a = list(map(int,input().split()))

f = [False]*n
b = [0]*n
max_ans = 0
set(0)

print(max_ans)

    

    
