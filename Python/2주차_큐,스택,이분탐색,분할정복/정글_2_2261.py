# 가장 가까운 두점
import sys

def dist(a,b):
    return (a[0]-b[0])**2 + (a[1]-b[1])**2

def search_min(a):
    ans = -1
    for i in range(len(a)-1):
        for j in range(i+1,len(a)):
            if ans == -1 or ans > dist(a[i],a[j]):
                ans = dist(a[i],a[j])
    return ans

def solve(a):
    if len(a)<5:
        ans = search_min(a)
    else:
        mid = len(a)//2
        ans = min(solve(a[:mid]),solve(a[mid+1:]))
        
        b = find_near_x(a,mid,ans)
        b.sort(key= lambda x:x[1])

        ans = find_near_y(b,ans)
    return ans

def find_near_x(a,point,ans_given):
    b=[a[point]]
    i = 1
    while(point+i<len(a)):
        if (a[point+i][0] - a[point][0])**2 <= ans_given:
            b.append(a[point+i])
            i += 1
        else:
            break
    i = 1
    while(point-i>=0):
        if (a[point][0] - a[point-i][0])**2 <= ans_given:
            b.append(a[point-i])
            i += 1
        else:   
            break
    return b
    
def find_near_y(a,ans_given):
    ans = ans_given
    for i in range(len(a)-1):
        for j in range(i+1,len(a)):
            if (a[i][1] - a[j][1])**2 < ans: 
                if ans > dist(a[i],a[j]):
                    ans = dist(a[i],a[j])
            else:
                break
    return ans

N = int(sys.stdin.readline())
A = []
for i in range(N):
    A.append(list(map(int,sys.stdin.readline().split())))
A.sort()
# print('*'*30)

ans = solve(A)
print(ans)





