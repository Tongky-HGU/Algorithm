# 트리순회
import sys

sys.setrecursionlimit(100000)
N = int(sys.stdin.readline())
inorder = list(map(int,sys.stdin.readline().split()))
postorder = list(map(int,sys.stdin.readline().split()))

# postorder의 끝값이 inorder에 어디에 위치해 있는지 확인하기 위해 인덱스 저장
idx = [0] * (N+1) 
for i in range(N):
    idx[inorder[i]] = i

def preorder(in_l,in_r,post_l,post_r):
    if in_l > in_r or post_l > post_r:
        return
    
    root = postorder[post_r] # postorder의 마지막은 항상 루트
    print(root, end =' ')

    p = idx[root]
    left = p - in_l
    preorder(in_l, p-1, post_l, post_l+left-1)
    preorder(p+1, in_r, post_l+left, post_r-1)


preorder(0,N-1,0,N-1)