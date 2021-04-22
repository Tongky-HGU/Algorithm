import sys
m, n, l = list(map(int,sys.stdin.readline().split()))
x = list(map(int,sys.stdin.readline().split()))

x.sort()
a=[]

for i in range(n):
    a.append(list(map(int,sys.stdin.readline().split())))

cnt = 0
for i in a:
    cl = 0
    cr = m-1
    low = i[0] -l +i[1]
    upp = i[0] +l -i[1]
    # print(str(low) + " " + str(upp))

    while(cl<=cr):
        mid = (cl+cr)//2
        # print(x[mid])
        if low <= x[mid] and x[mid] <= upp:
            cnt+=1
            break
        elif x[mid] < low:
            cl = mid +1
        else :
            cr = mid -1

print(cnt)



