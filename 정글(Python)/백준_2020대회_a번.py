#끝말잇기
import sys
N = int(sys.stdin.readline())
A =[]
A= list(map(str,sys.stdin.readline().split()))
init = A[0][0]
flag = True
for i in range(2,N):
    if init != A[i][0]:
        flag =False

if flag:
    print(1)
else:
    print(0)
