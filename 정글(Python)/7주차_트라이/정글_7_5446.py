#용량 부족
import sys

class node:
    def __init__(self,key):
        self.key = key
        self.child = {}
        self.delete = False
        self.protect = False
        self.leaf = False


class trie:
    def __init__(self):
        self.root = node(None)

    def insert(self,string,delete):
        cur_node = self.root
        if delete:
            cur_node.delete = True
        else:   
            cur_node.protect = True
        for char in string:
            if char not in cur_node.child:
                cur_node.child[char] = node(char)
            cur_node=cur_node.child[char]
            if delete:
                cur_node.delete = True
            else:   
                cur_node.protect = True
        if delete:
            cur_node.leaf = True


    def count_delete(self):
        global ans
        ans = 0
        def count(cur_node):
            global ans
            # print(cur_node.key)
            if cur_node.protect and cur_node.delete and cur_node.leaf:
                # print("+")
                ans +=1
            elif not cur_node.protect and cur_node.delete:
                # print("+")
                ans += 1
                return
            for _,next_node in cur_node.child.items():
                count(next_node)
        
        count(self.root)
        print(ans)

N = int(sys.stdin.readline())
for _ in range(N):
    trie1 = trie()
    N1 = int(sys.stdin.readline())
    for _ in range(N1):
        trie1.insert(str(sys.stdin.readline().rstrip()), True)
    N2 = int(sys.stdin.readline())
    for _ in range(N2):
        trie1.insert(str(sys.stdin.readline().rstrip()), False)
    
    trie1.count_delete()
        
