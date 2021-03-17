#분해합
import sys
N = int(sys.stdin.readline().rstrip())

def sol():
    for i in range(1,N,1):
        num = i
        ans = i
        while(num != 0):
            ans += num % 10
            num = num//10
            # print(ans)
        if (ans == N):
            print(i)
            return
    print(0)

sol()