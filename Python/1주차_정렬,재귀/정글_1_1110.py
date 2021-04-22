a = int(input())
count = 0
ans = a
while(1):
    count += 1
    if a< 10:
        s=[0]
        s.append(a)
    else:
        s= list(str(a))

    new_s = [int(s[1]),(int(s[0])+int(s[1]))%10]
    b = new_s[0]*10+new_s[1]
    if (ans == b):
        print(count)
        break
    else:
        a = b
    






