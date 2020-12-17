# 외판원 순회2 TSP

def cal(b):
    ans = 0
    for i in range(len(b)-1):
        if a[b[i]][b[i+1]] == 0 :
            ans = 10000000
        else:
            ans += a[b[i]][b[i+1]]
    return ans

def set(i):
    global min_sum
    for j in range(n):
        if f[j] == False:
            b.append(j)
            if i == n-1:
                b.append(b[0])
                if cal(b) < min_sum:
                    min_sum = cal(b)
                b.pop(-1)
            else:
                if cal(b) < min_sum:
                    f[j] = True
                    set(i+1)
                    f[j] = False
            b.pop(-1)

a=[]
n = int(input())
for i in range(n):
    a.append(list(map(int,input().split())))

f=[False]*n
b=[]
min_sum = 10000000
set(0)
print(min_sum)