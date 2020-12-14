#n 퀸
n=int(input())

pos = [0]*n
flag = [False]*n
flag_L = [False]*(2*n-1)
flag_R = [False]*(2*n-1)

def put():
    for i in range(n):
         print(pos[i],end="")
    print()

def set(count,i):
    for j in range(n):
        if not flag[j] and not flag_L[i+j] and not flag_R[n-1+i-j]:
            pos[i]=j
            if i == n - 1:
                # put()
                count +=1
            else:
                flag[j] = flag_L[i+j] = flag_R[n-1+i-j]=True
                count = set(count,i+1)
                flag[j] = flag_L[i+j] = flag_R[n-1+i-j]=False
    return count
count=0;
print(set(count,0))

