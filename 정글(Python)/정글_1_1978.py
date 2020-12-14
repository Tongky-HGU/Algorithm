n = int(input())
a = list(map(int,input().split()))
count =0
for i in range(n):
    if a[i] == 1:
        count+=1
    for j in range(2,a[i]):
        if a[i]%j == 0:
            count += 1
            break
print(n-count)