n = int(input())

strike = []
ball = []
for i in range(3):
    strike.append([0] *10)
    ball.append([0] *10)

for _ in range(n):
    score = list(map(int,input().split()))
    if score[1] >= 0:
        strike[0][score[0]//100] +=1
        strike[1][score[0]//10%10] +=1
        strike[2][score[0]%10] +=1
    if score[2] >= 0:
        ball[0][score[0]//100] +=1
        ball[1][score[0]//10%10] +=1
        ball[2][score[0]%10] +=1

for i in range(3):
    for j in range(10):
        if strike[i][j] >= 2:
            print(strike[i][j])
            ball[0][j] = 0
            ball[1][j] = 0
            ball[2][j] = 0



    

print(strike)
print(ball)







