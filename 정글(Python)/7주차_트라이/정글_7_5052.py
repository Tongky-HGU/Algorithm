#전화번호 목록
import sys

class node:
    def __init__(self,key,data=None):
        self.key = key
        self.data = data
        self.child = {}

class trie:
    def __init__(self):
        self.head = node(None)

    def insert(self,string):
        cur_node = self.head

        for char in string:
            if char not in cur_node.child:
                cur_node.child[char] = node(char)
            cur_node = cur_node.child[char]
            if cur_node.data != None:
                return False

        cur_node.data = string
        if cur_node.child:
            return False
        return True

N = int(sys.stdin.readline())

for _ in range(N):
    trie1 = trie()
    M = int(sys.stdin.readline())
    ans = True
    for _ in range(M):
        A = str(sys.stdin.readline().rstrip())
        temp = trie1.insert(A)
        if temp == False:
            ans = False
    if ans:
        print("YES")
    else:
        print("NO")
