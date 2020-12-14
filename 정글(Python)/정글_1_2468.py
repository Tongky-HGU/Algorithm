# 안전영역
a=[]
n = int(input())
for i in range(n):
    a.append(list(map(int,input().split())))

for i in range(n):
    for j in range(n):
        a[i][j] -= 3

for i in range(n):
    print(a[i])