# 색종이만들기
import sys 

def divide(n,i,j):
    global blue, white
    if n == 1:
        # print(str(i)+" "+str(j))
        if a[i][j] == 1:
            blue += 1
        else :
            white +=1
        return
    
    if a[i][j]== 1: check = 1
    else: check = 0

    fail = False

    for x in range(i,i+n):
        for y in range(j,j+n):
            if fail == False:
                if a[x][y] != check: fail = True; break
 
    if fail == True:
        divide(n//2,i,j)
        divide(n//2,i+(n//2),j)
        divide(n//2,i,j+(n//2))
        divide(n//2,i+(n//2),j+(n//2))
    else:
        if check == 1:
            blue+=1
        else: 
            white +=1

n1 = int(sys.stdin.readline())
a=[]
for i in range(n1):
    a.append(list(map(int,sys.stdin.readline().split())))

blue = 0
white = 0

divide(n1,0,0)

print(white)
print(blue)

