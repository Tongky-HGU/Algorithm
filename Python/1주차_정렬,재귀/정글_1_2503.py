n = int(input())

ans=[]
for _ in range(n):
    ans.append(list(map(int,input().split())))

a = [i for i in range(100,1000)]
# 0 다 제거 
for i in range(len(a)-1,-1,-1):
    if a[i]%10 == 0 or a[i]//10%10 == 0 or a[i]//100%10==0:
        a.pop(i)
# 겹치는 코드 다제거
for i in range(len(a)-1,-1,-1):
    if a[i]%10 == a[i]//10%10 or a[i]//10%10 == a[i]//100%10 or a[i]%10 == a[i]//100%10:
        a.pop(i)

for call, strike, ball in ans:
    for i in range(len(a)-1,-1,-1):
        # strike 비교
        a_strike = 0
        if a[i]%10 == call%10 : a_strike += 1
        if a[i]//10%10 == call//10%10: a_strike += 1
        if a[i]//100%10==call//100%10: a_strike += 1
        # ball 비교
        a_ball = 0
        if a[i]%10 == call//10%10 or a[i]%10 == call//100%10: a_ball += 1
        if a[i]//10%10 == call%10 or a[i]//10%10 == call//100%10: a_ball += 1
        if a[i]//100%10 == call%10 or a[i]//100%10 == call//10%10: a_ball += 1

        if(a_strike != strike or a_ball != ball): a.pop(i)

print(len(a))
    
        








