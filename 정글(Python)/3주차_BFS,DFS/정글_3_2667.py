# 단지 번호 붙이기
import sys
from collections import deque

N = int(sys.stdin.readline())

A=[]
for i in range(N):
    A.append(list(map(int,sys.stdin.readline().rstrip())))

vis=[[0 for _ in range(N)] for _ in range(N)]

print(A)
print(vis)

dr =[0,1,0,-1]
dc =[1,0,-1,0]

queue = deque()

while(queue)