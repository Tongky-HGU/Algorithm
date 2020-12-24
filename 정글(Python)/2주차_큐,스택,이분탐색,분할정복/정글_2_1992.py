#쿼드트리
import sys
N = int(sys.stdin.readline())
A=[]
ans=[]
for i in range(N):
    A.append(list(map(str,sys.stdin.readline().rstrip())))

def sol(n,i,j):

    if n == 1:
        return A[i][j]
    else:
        a = sol(n//2,i,j)
        b = sol(n//2,i,j+n//2)
        c = sol(n//2,i+n//2,j)
        d = sol(n//2,i+n//2,j+n//2)
        if len(a) +len(b)+len(c)+len(d) == 4:
            if int(a)*int(b)*int(c)*int(d) == 1:
                return '1'
            elif int(a)+int(b)+int(c)+int(d) == 0:
                return '0' 
            else:
                return '('+a+b+c+d+')'
        else:
            return '('+a+b+c+d+')'
        
print(sol(N,0,0))

