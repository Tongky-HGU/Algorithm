import sys

N, H = map(int,sys.stdin.readline().split())
A = [int(sys.stdin.readline()) for _ in range(N)]
high = [0 for _ in range(H+1)]
low = [0 for _ in range(H+1)]
total = [0 for _ in range(H+1)]

for idx,i in enumerate(A):
    if idx%2 == 1:
        high[i] +=1
    else:
        low[i] +=1

s = 0
for i in range(H,0,-1):
    s += high[i]
    total[H-i+1] += s

s = 0
for i in range(H,0,-1):
    s += low[i]
    total[i] += s

ans = min(total[1:])
num = len(list(filter(lambda x : x == ans,total[1:])))

print(ans, num)
