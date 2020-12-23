# 원 영역
import sys
limit_number = 150000
sys.setrecursionlimit(limit_number)

N= int(sys.stdin.readline())
A=[]
for i in range(N):
    x, r = map(int,sys.stdin.readline().split())
    A.append([x-r,0])
    A.append([x+r,1])

A.sort(key=lambda x:(x[0],-x[1]))
# print(A)

cnt = 1

def solve(i):
    # print("new")
    global cnt
    start=[]
    inner = 0
    outer = 0
    while(1):
        # print(A[i])
        if A[i][1] == 0:
            if len(start)==0:
                start.append(A[i])
            else:
                inner_receive, i = solve(i)
                inner += inner_receive
        else:
            outer = A[i][0] - start[0][0]
            if inner == outer:
                cnt+=2
                # print("cnt2")
            else:
                cnt+=1
                # print("cnt1")
            
            return outer, i
        i += 1 

_ , ptr = solve(0)

while(1):
    if ptr == len(A)-1:
        break
    _ , ptr = solve(ptr+1)

print(cnt)