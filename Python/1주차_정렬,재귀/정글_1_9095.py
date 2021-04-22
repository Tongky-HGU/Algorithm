def find(a):
    global ans
    if a == 3: ans += 4; return 
    elif a == 2: ans += 2;return 
    elif a == 1: ans += 1;return 
    elif a >= 0: 
        find(a-3)
        find(a-2)
        find(a-1)

n = int(input())

for _ in range(n):
    a = int(input())
    ans = 0
    find(a)
    print(ans)

