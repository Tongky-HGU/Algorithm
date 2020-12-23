# 수찾기
import sys
n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
b = list(map(int,sys.stdin.readline().split()))

a.sort()

def binary_search(target):
    cl = 0
    cr = n-1
    while(cl<=cr):
        mid = (cl+cr)//2
        if target > a[mid]:
            cl = mid+1
        elif target < a[mid]:
            cr = mid-1
        else:
            print(1)
            return mid
    print(0)
    return -1

for i in range(m):
    binary_search(b[i])