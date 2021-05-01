#주사위 굴리기
import sys
N, M , Y, X, K = map(int,sys.stdin.readline().split())
A = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
B = list(map(int,sys.stdin.readline().split()))

dice = [0] * 7
def move(direction):
    if direction == 1:
        dice[1], dice[3], dice[4], dice[6] = dice[3], dice[6], dice[1], dice[4]
    elif direction == 2:
        dice[1], dice[3], dice[4], dice[6] = dice[4], dice[1], dice[6], dice[3]
    elif direction == 3:
        dice[1], dice[2], dice[5], dice[6] = dice[2], dice[6], dice[1], dice[5]
    elif direction == 4:
        dice[1], dice[2], dice[5], dice[6] = dice[5], dice[1], dice[6], dice[2]

D = [[],[0,1],[0,-1],[-1,0],[1,0]]

dice[6] = A[Y][X]
A[Y][X] = 0
cur = [Y,X]
for b in B:
    cy = cur[0] + D[b][0]
    cx = cur[1] + D[b][1]
    if cy >= N or cy < 0 or cx >= M or cx < 0: continue
    move(b)
    if A[cy][cx] == 0:
        A[cy][cx] = dice[6]
    else:
        dice[6] = A[cy][cx] 
        A[cy][cx] = 0
    cur = [cy,cx]
    # print(dice)
    print(dice[1])
