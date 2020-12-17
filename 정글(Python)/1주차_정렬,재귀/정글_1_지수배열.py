# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
# 지수 정렬로 풀어봤음다


n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

n = len(a)
f = [0] * 10001
b = [0] * n

for i in range(n) : f[a[i]] += 1
for i in range(1,10001) : f[i] += f[i-1]
for i in range(n-1,-1,-1) : f[a[i]] -= 1; b[f[a[i]]] = a[i]

for i in range(n):
    print(b[i])