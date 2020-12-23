import sys

def solve(left,right):
    if left==right: return a[left]
    mid = (left+right)//2
    ans = max(solve(left,mid),solve(mid+1,right))
    cl, cr = mid,mid+1
    height = min(a[cl],a[cr])# 중간 사각형 고려
    ans = max(height*2,ans)
    while(cl>left or cr<right):
        if(cr<right and (cl==left or a[cl-1]<a[cr+1])):
            cr += 1
            height = min(height,a[cr])
        else:
            cl -= 1
            height = min(height,a[cl])
        ans = max(ans,height*(cr-cl+1))
    return ans

while(1):
    a = list(map(int,sys.stdin.readline().split())) 
    if a[0] == 0: break
    else:
        print(solve(1,a[0]))
        
        

