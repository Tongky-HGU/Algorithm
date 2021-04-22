#문자열집합
import sys

class node:
    def __init__(self,key,data=None):
        self.key = key
        self.data = data
        self.child={}

class trie:
    def __init__(self):
        self.root = node(None)
    def insert(self,string):
        cur_node = self.root

        for char in string:
            if char not in cur_node.child:
                cur_node.child[char] = node(char)
            cur_node = cur_node.child[char]
        
        cur_node.data = string

    def search(self,string):
        cur_node = self.root

        for char in string:
            if char not in cur_node.child:
                return 0
            cur_node = cur_node.child[char]
            
        if cur_node.data == string:
            return 1


N, M = map(int,sys.stdin.readline().split())
trie1 = trie()
ans = 0

for _ in range(N):
    trie1.insert(str(sys.stdin.readline().rstrip()))

for _ in range(M):
    if trie1.search(str(sys.stdin.readline().rstrip())):
        ans += 1

print(ans)

    