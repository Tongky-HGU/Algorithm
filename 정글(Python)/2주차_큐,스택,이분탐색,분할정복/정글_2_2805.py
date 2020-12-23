# 나무자르기
# 나무를 sorting 하고 거꾸로 내려왔으면 
import sys

def count_tree(h):
    tree = 0
    for i in range(n):
        if a[i] > h:
            tree += (a[i] - h)
    return tree

def binarysearch(ans):
    max_height = 0
    cl = 0
    cr = max(a)
    while cl <= cr:
        mid = (cl+cr)//2

        if  count_tree(mid) >= ans:
            max_height = mid
            cl = mid +1
        else:
            cr = mid -1
    print(int(max_height))
    return   

n, ans = list(map(int,sys.stdin.readline().split()))
a = list(map(int,sys.stdin.readline().split()))

binarysearch(ans)
