import math

def solution(begin, target, words):
    global ans 
    ans = math.inf
    N = len(words)
    word_length = len(begin)
    words = [begin] + words
    vis = [0]*(N+1)
    # print(words)
    def dfs(i,cnt):
        global ans 
        vis[i] = 1
        for j in range(1,N+1):
            if vis[j] == 0:
                word_cnt = 0
                for k in range(word_length):
                    if words[j][k] == words[i][k]:
                        word_cnt +=1
                if word_cnt == word_length -1:
                    
                    if words[j] == target:
                        # print(words[i])
                        ans = min(ans, cnt+1)
                        return
                
                    dfs(j, cnt+1)
                
    dfs(0,0)
    
    if ans == math.inf:
        return 0
    else:
        return ans