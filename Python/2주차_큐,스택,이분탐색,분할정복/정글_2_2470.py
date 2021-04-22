import sys 
        
n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
a.sort()

cl = 0
cr = n-1
ans = a[cl]+a[cr]
ans_c = [a[cl], a[cr]]

while(cl < cr):
    sum1 = a[cl]+a[cr]

    if sum1 == 0 :
        ans = sum1
        ans_c = [a[cl], a[cr]]
        break
    elif abs(sum1) < abs(ans) :
        ans = sum1
        ans_c = [a[cl], a[cr]]

    if sum1 > 0 :
        cr -= 1
    else:
        cl += 1

print(*ans_c)