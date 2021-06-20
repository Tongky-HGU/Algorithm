# 블록이동하기
# 아예 예외처리안해도되게 1줄 그냥 바깥에 그어놓는 것도 방법...
from collections import deque

def move(cur1,cur2,newBoard):
    Y,X  = 0,1
    cand = []
    dx = [1,0,-1,0]
    dy = [0,-1,0,1]
    for i in range(4):
        nxt1 = (cur1[Y] + dy[i], cur1[X] + dx[i])
        nxt2 = (cur2[Y] + dy[i], cur2[X] + dx[i])
        if newBoard[nxt1[Y]][nxt1[X]] == 0 and newBoard[nxt2[Y]][nxt2[X]] == 0:
            cand.append((nxt1, nxt2))
    
    if cur1[Y] == cur2[Y]: 
        UP, DOWN = -1, 1
        for d in [UP, DOWN]:
            if newBoard[cur1[Y]+d][cur1[X]] == 0 and newBoard[cur2[Y]+d][cur2[X]] == 0:
                cand.append((cur1, (cur1[Y]+d, cur1[X])))
                cand.append((cur2, (cur2[Y]+d, cur2[X])))
    else:
        LEFT, RIGHT = -1, 1
        for d in [LEFT, RIGHT]:
            if newBoard[cur1[Y]][cur1[X]+d] == 0 and newBoard[cur2[Y]][cur2[X]+d] == 0:
                cand.append(((cur1[Y], cur1[X]+d), cur1))
                cand.append(((cur2[Y], cur2[X]+d), cur2))

    return cand


def solution(board):
    N = len(board)
    newBoard = [[ 1 for _ in range(N+2)] for _ in range(N+2)]
    for i in range(N):
        for j in range(N):
            newBoard[i+1][j+1] = board[i][j]
        
    queue = deque([((1, 1), (1, 2), 0)])
    vis = set([((1, 1), (1, 2))])

    while queue:
        cur1,cur2,cnt = queue.popleft()
        if cur1 == (N,N) or cur2 == (N,N):
            return cnt
        for nxt in move(cur1,cur2,newBoard):
            if nxt not in vis:
                queue.append((*nxt,cnt+1))
                vis.add(nxt)

print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))


# # 블록이동하기
# import math
# from collections import deque
# COL = 0
# BAR = 1

# def solution(board):
#     ans = math.inf
#     newBoard = [[1 for _ in range(len(board)+1)] for _ in range(len(board)+1)]
#     for i in range(len(board)):
#         for j in range(len(board)):
#             if board[i][j] == 0 :
#                 newBoard[i][j] = 0
#     board= newBoard
#     N = len(board)
#     vis = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(2)]
#     dr = [0,1,0,-1]
#     dc = [1,0,-1,0]

#     queue = deque()
#     vis[BAR][0][0]
#     queue.append([0,0,BAR,0])
#     while(queue):
#         r,c,mode,cnt = queue.popleft()
#         # print(r,c,mode,cnt)
#         if mode == BAR:
#             if r == N-2 and c == N-3:
#                 ans = min(ans,cnt)

#             for i in range(4):
#                 cr = r + dr[i]
#                 cc = c + dc[i]
#                 if cr < 0 or cr >= N or cc < 0 or cc+1 >= N: continue
#                 if board[cr][cc] == 1 or board[cr][cc+1] == 1: continue
#                 if vis[BAR][cr][cc] : continue
#                 vis[BAR][cr][cc] = 1
#                 queue.append([cr,cc,BAR,cnt+1])
#             if r-1 > 0:
#                 if board[r-1][c] == 0 and board[r-1][c+1] == 0:
#                     if not vis[COL][r-1][c]:
#                         vis[COL][r-1][c] = 1
#                         queue.append([r-1,c,COL,cnt+1])

#                     if not vis[COL][r-1][c+1]:
#                         vis[COL][r-1][c+1] = 1
#                         queue.append([r-1,c+1,COL,cnt+1])
#             if r+1 < N: 
#                 if board[r+1][c] == 0 and board[r+1][c+1] == 0:
#                     if not vis[COL][r][c]:
#                         vis[COL][r][c] = 1
#                         queue.append([r,c,COL,cnt+1])
#                     if not vis[COL][r][c+1]:
#                         vis[COL][r][c+1] = 1
#                         queue.append([r,c+1,COL,cnt+1])
#         else:
#             if r == N-3 and c == N-2:
#                 ans = min(ans,cnt)

#             for i in range(4):
#                 cr = r + dr[i]
#                 cc = c + dc[i]
#                 if cr < 0 or cr+1 >= N or cc < 0 or cc >= N: continue
#                 if board[cr][cc] == 1 or board[cr+1][cc] == 1: continue
#                 if vis[COL][cr][cc] : continue
#                 vis[COL][cr][cc] = 1
#                 queue.append([cr,cc,COL,cnt+1])
#             if c-1 > 0:
#                 if board[r][c-1] == 0 and board[r+1][c-1] == 0:
#                     if not vis[BAR][r][c-1]:
#                         vis[BAR][r][c-1] = 1
#                         queue.append([r,c-1,BAR,cnt+1])

#                     if not vis[BAR][r+1][c-1]:
#                         vis[BAR][r+1][c-1] = 1
#                         queue.append([r+1,c-1,BAR,cnt+1])
#             if c+1 < N: 
#                 if board[r][c+1] == 0 and board[r+1][c+1] == 0:
#                     if not vis[BAR][r][c]:
#                         vis[BAR][r][c] = 1
#                         queue.append([r,c,BAR,cnt+1])

#                     if not vis[BAR][r+1][c]:
#                         vis[BAR][r+1][c] = 1
#                         queue.append([r+1,c,BAR,cnt+1])
#     return ans