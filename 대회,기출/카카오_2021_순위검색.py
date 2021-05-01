#순위검색
def solution(info, query):
    root = {}
    ans = []
    
    for Q in info:
        Q = list(Q.split(' '))
        Q = filter(lambda x : x != 'and',Q)
        now = root
        for index, cond in enumerate(Q):
            if cond in now:
                if index == 4:
                    now[cond] +=1
                now = now[cond]
            else:
                if index != 4:
                    now[cond] = {}
                    now = now[cond]
                else:
                    now[cond] = 1
                
    # print(root)
    
    for Q in query:
        Q = list(Q.split(' '))
        Q = filter(lambda x : x != 'and',Q)
        cnt = 0
        queue = []
        queue.append(root)
        for index, cond in enumerate(Q):
            temp = []
            
            while(queue):
                now = queue.pop()
                if index == 4:
                    for key,value in now.items():
                        if int(key) >= int(cond):
                            cnt += value
                if cond == "-":
                    for i in now:
                        temp.append(now[i])
                if cond in now:
                    temp.append(now[cond])

            queue = temp           
              
        ans.append(cnt)
    return ans   