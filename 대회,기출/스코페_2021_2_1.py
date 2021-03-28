import sys 
N , K = map(str,sys.stdin.readline().rstrip().split())
N = int(N)

# 연습 시간
time = 0
for i in range(3):
    a = int(K.split(":")[i])
    time += a * 60**(2-i)
# print(time)

# 트랙 시간
A = []
for _ in range(N):
    a = str(sys.stdin.readline().rstrip())
    temp = 0
    for i in range(2):
        b = int(a.split(":")[i])
        temp += b * 60**(1-i)   

    A.append(temp)
# print(A)

# 윈도우
ans_num = 0
ans_start = 0

temp = A[0] + 1
cnt = 2
cl = 0
cr = 1
while(cr != N):
    # print(f"{cl} {cr} {temp} {cnt}")
    if temp <= time:
        if cnt > ans_num:
            ans_num = cnt
            ans_start = cl
        # print("change!")
        cr += 1
        temp += A[cr-1]
        cnt += 1
    else:
        cl += 1
        temp -= A[cl-1]
        cnt -= 1
print(f"{ans_num} {ans_start+1}")