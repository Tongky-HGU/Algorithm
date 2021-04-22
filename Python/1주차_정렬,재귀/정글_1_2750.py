# 수정렬하기1
n = int(input())
ans = []
for i in range(n):
    a = int(input())
    if len(ans) == 0:
        ans.insert(0,a)
    else:
        last = 0
        for j in range(len(ans)):
            if a > ans[j]:
                last = j +1
        ans.insert(last,a)

for i in range(len(ans)):
    print(ans[i])