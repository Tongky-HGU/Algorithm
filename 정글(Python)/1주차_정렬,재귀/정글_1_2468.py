# 안전영역
n = int(input())

a=[]
for i in range(n):
    a.append(list(map(int,input().split())))

dx=[1,0,-1,0]
dy=[0,1,0,-1,0]

ans = 0

for water in range(0,102):

    vis=[]
    for i in range(n):
        vis.append([False]*n)

    mx = 0 
    for i in range(n):
        for j in range(n):
            if not vis[i][j] and a[i][j]>water :
                Q = []
                Q.append([i,j])
                mx += 1
                while(len(Q)!=0):
                    for di in range(len(dx)):
                        cur_x = Q[0][0] + dx[di]
                        cur_y = Q[0][1] + dy[di]

                        if(cur_x < 0 or cur_x >= n or cur_y < 0 or cur_y >= n): continue
                        if(vis[cur_x][cur_y] or a[cur_x][cur_y]<=water): continue
                        Q.append([cur_x,cur_y])
                        vis[cur_x][cur_y] = True
                    Q.pop(0)
    ans = max(ans,mx)
    if(mx == 0): break

# for i in range(n):
#     print(a[i])
#     print(vis[i])

print(ans)



