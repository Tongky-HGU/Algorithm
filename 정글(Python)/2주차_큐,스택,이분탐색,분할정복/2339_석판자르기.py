#석판자르기
import sys
N = int(sys.stdin.readline())

A = [ list(map(int,sys.stdin.readline().split())) for _ in range(N)]

def dfs(start,end,direction):
    # print("---------------------") 
    # print(start)
    # print(end)
    # print(direction)
    jewelry = 0
    impurity = 0
    for i in range (start[0],end[0]+1):
        for j in range(start[1],end[1]+1):
            if A[i][j] == 1:
                impurity += 1
            elif A[i][j] == 2:
                jewelry +=1
    
    if (jewelry ==0): return 0
    elif (jewelry == 1 and impurity ==0 ): return 1

    cnt = 0

    for i in range (start[0],end[0]+1):
        for j in range(start[1],end[1]+1):
            if A[i][j] == 1:
                if direction == 1: 
                    # print("세로")
                    check = 0
                    for k in range(start[0],end[0]+1):
                        if A[k][j] == 2 : check+=1
                    if check == 0:
                        a = dfs([start[0],start[1]],[end[0],j-1],-1*direction)
                        b = dfs([start[0],j+1],[end[0],end[1]],-1*direction)
                        cnt += a*b
                else:
                    # print("가로")
                    check = 0
                    for k in range(start[1],end[1]+1):
                        if A[i][k] == 2 : check+=1
                    if check == 0:
                        a = dfs([start[0],start[1]],[i-1,end[1]],-1*direction) 
                        b = dfs([i+1,start[1]],[end[0],end[1]],-1*direction)
                        cnt += a*b
    return cnt

ans = 0
ans += dfs([0,0],[N-1,N-1],1)
ans += dfs([0,0],[N-1,N-1],-1)

# print(f"ans:{ans}")

if ans == 0:
    print(-1)
else:
    print(ans)
