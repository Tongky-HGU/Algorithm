#생태학
import sys 

class node:
    def __init__(self,key,data=None):
        self.key = key
        self.data = data
        self.cnt = 0
        self.child = {}
    
class trie:
    def __init__(self):
        self.root = node(None);
        self.total_cnt = 0

    def insert(self,string):
        cur_node = self.root
        self.total_cnt += 1
        for char in string:
            if char not in cur_node.child:
                cur_node.child[char] = node(char)
            cur_node = cur_node.child[char]
        cur_node.data = string
        cur_node.cnt += 1
    
    def print(self):
        def print_trie(cur_node):
            for key,next_node in sorted(cur_node.child.items()):
                if next_node.cnt != 0:
                    print(next_node.data,end=" ")
                    # print(round((next_node.cnt/self.total_cnt*100),4))
                    print("%.4f" %(next_node.cnt/self.total_cnt*100))
                    
                print_trie(next_node)

        print_trie(self.root)
        

trie1 = trie()

while(1):
    A = str(sys.stdin.readline().rstrip())
    
    if not A:
        break

    trie1.insert(A)

trie1.print()

        