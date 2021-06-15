#카드짝 맞추기
import math,copy
from collections import deque
from itertools import permutations

def solution(board, r, c):
    ans = math.inf

    N= set()
    [[ N.add(i) for i in row if i>0] for row in board]

    combis = permutations(N,len(N))

    for combi in combis:
        paths = []
        for i in combi:
            A,B = find(i,board)
            if not paths:
                paths.append([[A,B]])
                paths.append([[B,A]])
            else:
                temp = []
                for path in paths:
                    temp.append(path+[[A,B]])
                    temp.append(path+[[B,A]])
                paths = temp
        
        for path in paths:
            # print(path)
            myBoard = init(board)
            
            dist = 0
            cr ,cc =  r, c
            for to1, to2 in path:
                dist += bfs(cr,cc,to1[0],to1[1],myBoard)
                dist += bfs(to1[0],to1[1],to2[0],to2[1],myBoard)
                delelte(to1[0],to1[1],myBoard)
                delelte(to2[0],to2[1],myBoard)
                cr, cc = to2[0],to2[1]
            # print(dist)
            ans = min(dist,ans)
    return ans
    

def init(board):
    myBoard = copy.deepcopy(board)
    return myBoard

def find(number,board):
    ret = []
    for i in range(4):
        for j in range(4):
            if board[i][j] == number:
                ret.append([i,j])
    return ret

def delelte(tr,tc,board):
    board[tr][tc] = 0

def bfs(sr,sc,tr,tc,board):
    ret = math.inf
    dr = [1,0,-1,0]
    dc = [0,-1,0,1]
    vis = [[0 for _ in range(4)] for _ in range(4)]

    queue = deque()
    queue.append([sr,sc,0])
    vis[sr][sc] = 1
    while(queue):
        # print(queue)
        r,c,cnt = queue.popleft()
        if r == tr and c == tc:
            ret = min(ret,cnt)
            continue
        for i in range(4):
            cr = r +dr[i]
            cc = c +dc[i]
            if cr < 0 or cr > 3 or cc < 0 or cc > 3: continue
            if vis[cr][cc] != 1:
                vis[cr][cc] = 1
                queue.append([cr,cc,cnt+1])
        
            # ctrl
            while(1):
                cr = cr +dr[i]
                cc = cc +dc[i]
                if cr < 0 or cr > 3 or cc < 0 or cc > 3: 
                    cr = cr -dr[i]
                    cc = cc -dc[i]
                    break
                if board[cr][cc] > 0 : break

            if vis[cr][cc] != 1 :
                vis[cr][cc] = 1
                queue.append([cr,cc,cnt+1])
    return ret + 1