# 행렬테두리 회전하기
# stack으로 넣으면 좀더 직관적이게 풀 수 있더라

import math

def rotate(A,queries):
    r1,c1,r2,c2 = queries
    ret = math.inf
    direction = [[0,1],[1,0],[0,-1],[-1,0]]
    temp = A[r1-1][c1-1]
    curDirection = -1
    cur = [r1-1,c1-1]
    while(1):
        if cur[0]+1 == r1 and (cur[1]+1 == c1 or cur[1]+1 == c2):
            curDirection += 1
        elif cur[0]+1 == r2 and (cur[1]+1 == c1 or cur[1]+1 == c2):
            curDirection += 1
            
        cur[0] += direction[curDirection][0]
        cur[1] += direction[curDirection][1]
        
        ret = min(ret,temp)
        
        A[cur[0]][cur[1]], temp = temp, A[cur[0]][cur[1]] 
        
        if cur == [r1-1,c1-1] : break 
            
    return ret 

def solution(rows, columns, queries):
    ans = []
    A = [[0 for _ in range(columns)] for _ in range(rows)]
    num = 0
    for i in range(rows):
        for j in range(columns):
            num +=1
            A[i][j] = num
    # print(A)

    for query in queries:
        ans.append(rotate(A,query))
    # print(A)
    return ans