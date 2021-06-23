def solution(n, costs):
    cnt = 0
    ans = 0
    parent = [i for i in range(n)]
    
    def find(a):
        if parent[a] == a:
            return a
        parent[a] = find(parent[a])
        return parent[a]
    
    def union(a,b):
        a = find(a)
        b = find(b)
        if a == b: return False
        parent[a] = b
        return True
    
    costs.sort(key = lambda x : x[2])
    
    for a,b,d in costs:
        # print(a,b,d)
        if (union(a,b)):
            cnt += 1
            ans += d
            if cnt == n:
                return ans
            
    return ans