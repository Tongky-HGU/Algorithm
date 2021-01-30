import sys
sys.setrecursionlimit(30000)

class node:
    def __init__(self,key):
        self.key = key
        self.child = {}
        self.cache = {}
        
class trie:
    def __init__(self):
        self.root = node(None)

    def insert(self,string):
        cur_node=self.root
        N=len(string)
        for char in string:
            if N not in cur_node.cache:
                cur_node.cache[N] = 0
            cur_node.cache[N] += 1
            
            if char not in cur_node.child:
                cur_node.child[char] = node(char)
            cur_node = cur_node.child[char]
        
    def search(self,string):
        global ans
        N = len(string)
        ans = 0
        flag = False        
        
        def dfs(cur_node,level,N):
            global ans
            # print("*"*20)
            # print(string[level])
            # print(cur_node.key)

            if level == N-1:
                if cur_node.flag:
                    ans += 1
                    return
                else:       
                    return
                
            if string[level+1]=="?":
                if N in cur_node.cache:
                    ans += cur_node.cache[N]
                    return
                else:
                    return
                
                for key,next_node in cur_node.child.items():
                    dfs(next_node,level+1,N)
            else:
                if string[level+1] in cur_node.child:
                    dfs(cur_node.child[string[level+1]],level+1,N)
            return
        
        dfs(self.root,-1,N)
        
        # print(ans)
        return ans
        
def solution(words, queries):
    trie1 = trie()
    trie2 = trie()
    
    answer = []
    
    for word in words:
        trie1.insert(word)
        trie2.insert(word[::-1])
        
    for query in queries:
        if query[0] != '?':
            answer.append(trie1.search(query))
        else:
            answer.append(trie2.search(query[::-1]))
                    
    return answer