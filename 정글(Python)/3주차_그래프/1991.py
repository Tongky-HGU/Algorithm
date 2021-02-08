#트리 순회
import sys

N = int(sys.stdin.readline())
X = {} 
for _ in range(N):
    A, B, C = map(str,sys.stdin.readline().split())
    X[A] = [B,C]

# print(X)

def preorder(a):
    if a == '.':
        return
    print(a,end='')
    preorder(X[a][0])
    preorder(X[a][1])

def inorder(a):
    if a == '.':
        return
    inorder(X[a][0])
    print(a,end='')
    inorder(X[a][1])

def postorder(a):
    if a == '.':
        return
    postorder(X[a][0])
    postorder(X[a][1])
    print(a,end='')

preorder('A')
print('')
inorder('A')
print('')
postorder('A')
print('')




# class node:
#     def __init__(self):
#         self.key = None
#         self.left = None
#         self.right = None
    
#     def insert(self, key):
#         if self.key is not None:
#             if ord(key) < ord(self.key):
#                 if self.left is None:
#                     self.left = node()
#                     self.left.insert(key)
#                 else:
#                     self.left.insert(key)
#             elif ord(key) > ord(self.key):
#                 if self.right is None:
#                     self.right = node()
#                     self.right.insert(key)
#                 else:
#                     self.right.insert(key)
#         else:
#             print(self.key)
#             self.key = key