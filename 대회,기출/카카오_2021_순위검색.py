def solution(info, query):
    ans = []
    A = ["cpp", "java", "python"]
    B = ["backend", "frontend"]
    C = ["junior", "senior"]
    D = ["chicken", "pizza"]    
    
    data = {}
    
    for a in A:
        for b in B:
            for c in C:
                for d in D:
                    data[a+" "+b+" "+c+" "+d] = []
    
    for string in info:
        temp = string.split()
        data[" ".join(temp[0:4])].append(int(temp[4]))
    
    for d,k in data.items():
        k.sort(reverse=True)
    
    # print(data)
    
    def check(i,A):
        if i == "-":
            return A
        else:
            return [i]
        
    def bisect(a,x):
        cl = 0
        cr = len(a)
        while cl < cr:
            mid = (cl+cr) //2
            if a[mid] >= x: cl = mid + 1
            else: cr = mid
        return cl
        
    for string in query:
        cnt = 0
        temp = string.split(" ")
        temp = list(filter(lambda x : x != "and",temp))
    
        for a in check(temp[0],A):
            for b in check(temp[1],B):
                for c in check(temp[2],C):
                    for d in check(temp[3],D):
                        if(data[a+" "+b+" "+c+" "+d]):
                            index = bisect(data[a+" "+b+" "+c+" "+d],int(temp[4]))
                            cnt += index
        ans.append(cnt)
                    
    return ans