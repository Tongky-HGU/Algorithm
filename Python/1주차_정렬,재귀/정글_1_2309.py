# 백설공주
def find_ans(a):
    for i in range(9):
        for j in range(i+1,9):
            if(a[i]+a[j]==ans):
                a.pop(j)
                a.pop(i)
                return a

a= []
for i in range(9):
    a.append(int(input()))
ans = sum(a)-100
find_ans(a)
for i in sorted(a):
    print(i)