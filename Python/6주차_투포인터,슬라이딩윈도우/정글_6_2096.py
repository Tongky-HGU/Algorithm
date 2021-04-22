#내려가기
import sys

N = int(sys.stdin.readline())
A = [0 for _ in range(3)]
A = [A] + [ list(map(int,sys.stdin.readline().split())) for _ in range(N)]

# print(A)
ans_min_p = [ 0 for _ in range(3)]
ans_min_n = [ 0 for _ in range(3)]

ans_max_p = [ 0 for _ in range(3)]
ans_max_n = [ 0 for _ in range(3)]

for i in range(1,N+1):

    ans_min_n[0] = min(ans_min_p[0],ans_min_p[1]) + A[i][0]
    ans_min_n[1] = min(ans_min_p) + A[i][1]
    ans_min_n[2] = min(ans_min_p[1] ,ans_min_p[2]) + A[i][2]
    ans_min_p = ans_min_n[:]

    ans_max_n[0] = max(ans_max_p[0],ans_max_p[1]) + A[i][0]
    ans_max_n[1] = max(ans_max_p) + A[i][1]
    ans_max_n[2] = max(ans_max_p[1] ,ans_max_p[2]) + A[i][2]
    ans_max_p = ans_max_n[:]

print(str(max(ans_max_n))+" "+str(min(ans_min_n)))

    
