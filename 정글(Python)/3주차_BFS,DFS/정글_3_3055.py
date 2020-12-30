#탈출
import sys
from collections import deque

R, C = map(int,sys.stdin.readline().split())
A = []*R
for i in range(R):
    A.append(list(str(sys.stdin.readline().rstrip())))

dr = [1,0,-1,0]
dc = [0,-1,0,1]

vis = [[0 for _ in range(C)] for _ in range(R)]
hedgehog = deque()
water = deque()
safehouse = 0

for i in range(R):
    for j in range(C):
        if A[i][j] == 'S':
            hedgehog.append([i,j])
            vis[i][j] = 1
        elif A[i][j] == '*':
            water.append([i,j])
            vis[i][j] = 1
        elif A[i][j] == 'D':
            safehouse = [i,j]

def sol():
    hour = 0
    flag = False
    while(1):
        cursize = len(water)
        while(cursize):
            cur = water.popleft()
            # print("water:" + str(cur))
            for i in range(4):
                cr = cur[0] + dr[i]
                cc = cur[1] + dc[i]
                if cr < 0 or cr >= R or cc < 0 or cc >= C : continue
                if vis[cr][cc] == 1: continue
                if A[cr][cc] == 'D' or A[cr][cc] == 'X' : continue
                water.append([cr,cc])
                vis[cr][cc] = 1
            cursize -= 1

        cursize = len(hedgehog)
        while(cursize):
            cur = hedgehog.popleft()
            # print("hedge:" + str(cur))
            if cur == safehouse:
                flag = True
                break
            for i in range(4):
                cr = cur[0] + dr[i]
                cc = cur[1] + dc[i]
                if cr < 0 or cr >= R or cc < 0 or cc >= C : continue
                if vis[cr][cc] == 1: continue
                if A[cr][cc] == '*' or A[cr][cc] == 'X' : continue
                hedgehog.append([cr,cc])
                vis[cr][cc] = 1
            cursize -= 1
        if flag == True:
            print(hour)
            break
        if len(hedgehog)==0:
            print("KAKTUS")
            break
        hour +=1

sol()