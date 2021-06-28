import sys
sys.setrecursionlimit(3000)
def solution(s):
    def dfs(a,b):
        if b < a: return True
        if s[a] == s[b]: return dfs(a+1,b-1)
        else: return False
    
    for cut in range(len(s),0,-1):
        for start in range(len(s)):
            if start + cut >= len(s): break
            if dfs(start,start+cut):
                print(start,start+cut)
                return cut + 1
    return 1
    

print(solution("zxcvasdfqwer"))