# 뱀
import sys
from collections import deque
N = int(sys.stdin.readline())

A = int(sys.stdin.readline())
a = []
for i in range(A):
    a.append(list(map(int,sys.stdin.readline().split())))
    a[-1][0] -=1
    a[-1][1] -=1

T = int(sys.stdin.readline())
t = []
for i in range(T):
    t.append(list(map(str,sys.stdin.readline().split())))

def go():
    snake.append([snake[-1][0]+direction[0],snake[-1][1] +direction[1]])
    snake.popleft()

def eat():
    snake.append([snake[-1][0]+direction[0],snake[-1][1] +direction[1]])

def turn(turn_dir):
    global direction_ptr,direction
    if turn_dir == 'L':
        direction_ptr +=1
        if direction_ptr > 3 :
            direction_ptr = 0
        direction = directions[direction_ptr]
    else:
        direction_ptr -=1
        if direction_ptr < 0 :
            direction_ptr = 3
        direction = directions[direction_ptr]


snake = deque([[0,0]])
direction_ptr = 0
direction = [0,1]
directions = [0,1],[-1,0],[0,-1],[1,0]

seconds = 0
while(1):
    seconds+=1

    #자기 꼬리 확인
    if snake.count([snake[-1][0]+direction[0],snake[-1][1] +direction[1]])>0:
        break

    #사과
    apple = False
    for i in range(len(a)):
        if snake[-1] == a[i]:
            apple = True
            a.pop(i)
            break
    if apple:
        eat()
    else:
        go()
    
    #모서리 확인
    if snake[-1][0] < 0 or snake[-1][0] >= N or snake[-1][1] < 0 or snake[-1][1]>= N:
        break
    
    #방향
    if len(t) > 0:
        if seconds == int(t[0][0]):
            turn(t[0][1])
            t.pop(0)

print(seconds)