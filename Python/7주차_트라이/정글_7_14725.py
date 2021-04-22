#개미굴
import sys

class node:
    def __init__(self,key,data=None):
        self.key = key
        self.child = {}

class trie:
    def __init__(self):
        self.root = node(None)
    
    def insert(self,food_list):
        cur_node = self.root

        for food in food_list:
            if food not in cur_node.child:
                cur_node.child[food] = node(food)
            cur_node = cur_node.child[food]
    
    def print(self):

        def print_trie(cur_node,level):
            for key,child_node in sorted(cur_node.child.items()):
                print("--"*level,end="")
                print(key)
                print_trie(child_node,level+1)
        
        print_trie(self.root,0)


N = int(sys.stdin.readline())
trie1 = trie()
for _ in range(N):
    A = list(map(str,sys.stdin.readline().split()))
    trie1.insert(A[1:])

trie1.print()