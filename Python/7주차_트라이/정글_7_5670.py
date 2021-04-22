#휴대폰 자판
import sys

class node:
    def __init__(self, key):
        self.key = key
        self.data = False
        self.child = {}

class trie:
    def __init__(self):
        self.root = node(None)

    def insert(self,string):
        cur_node = self.root
        for char in string:
            if char not in cur_node.child:
                cur_node.child[char] = node(char)
            cur_node = cur_node.child[char]
        cur_node.data = True
        
            
    def count(self,string):
        cur_node = self.root
        cnt = 0
        for char in string:
            cur_node = cur_node.child[char]
            if len(cur_node.child)> 1 or cur_node.data:
                cnt +=1
        return cnt


while(1):
    try:
        N = int(sys.stdin.readline())
    except:
        break

    trie1 = trie()
    A=[]
    cnt=0
    for i in range(N):
        A.append(str(sys.stdin.readline().rstrip()))
        trie1.insert(A[i])
    
    for i in range(N):
        cnt += trie1.count(A[i])

    print("%.2f" %(cnt/N))
        