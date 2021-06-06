# 리모컨
import sys, math
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
A = set(map(int,sys.stdin.readline().split())) if M else set()

# 근접거리 부터 탐색 -> 반례
# 결국 부르트포스
# 1. 그냥 위아래로만 
ans = min(math.inf, abs(100-N))

# 2. 숫자로만
string = str(N)
flag = True
for char in string:
    if int(char) in A:
        flag = False
        break
if(flag):
    ans = min(ans,len(string))
    print(ans)
    exit()

# 3. 숫자로 가고 위아래 버튼으로 갔을때
for i in range(0,1000000):
    if abs(i - N) > ans: continue
    string = str(i)
    flag = True
    for char in string:
        if int(char) in A:
            flag = False            
            break
    if(flag):
        ans = min(ans, abs(i - N)+len(string))

print(ans)