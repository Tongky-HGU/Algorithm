# Z
 

n, r ,c = map(int,input().split())

def z(n, i,j):
    global count
    if  i+n-1 < r or j+n -1 < c:
        count += n**2
        return 
    elif r < i or c < j:
        return
    else:
        if (n == 2):
            a =[[i,j],[i,j+1],[i+1,j],[i+1,j+1]]
            for x, y in a:
                if (int(x) == r and int(y) == c):
                    print(count)
                    return
                count+=1
                # print("{} {}".format(x,y))
        else:
            z(n//2,i,j)
            z(n//2,i,j+n//2)
            z(n//2,i+n//2,j)
            z(n//2,i+n//2,j+n//2)

count = 0
z(2**n,0,0)



   # if j+1 < (2**n)-1:
    #     count = z(n,i,j+2,r,c)
    # elif i+1 < (2**n)-1:
    #     count = z(n,i+2,0,r,c)