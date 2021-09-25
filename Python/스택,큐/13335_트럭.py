import sys
from collections import deque

N, L, W = map(int,sys.stdin.readline().split())
A = deque(map(int,sys.stdin.readline().split()))

bridge = deque()
cnt = 0
while(1):
    cnt += 1
    for car in bridge:
        car[1] += 1

    if bridge and bridge[0][1] > L:
        W += bridge.popleft()[0]

    if A and W >= A[0]:
        newCar = A.popleft()
        bridge.append([newCar,1])
        W -= newCar

    if not bridge and not A:
        break
print(cnt)