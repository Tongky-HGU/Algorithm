#후보키
# discard하면 에러가 안남

from itertools import combinations

def solution(relation):
    R = len(relation)
    C = len(relation[0])
    
    combis = []
    for i in range(1,C+1):
        combis.extend(combinations(range(C),i))
    
    # 유일성
    unique = [] 
    for combi in combis:
        tmp = [tuple([items[i] for i in combi]) for items in relation]
        if len(set(tmp)) == R:
            unique.append(combi)
            
    # print(unique)
    
    #최소성
    ans = set(unique)
    for i in range(len(unique)):
        for j in range(i+1,len(unique)):
            if len(unique[i]) == len(set(unique[i]) & set(unique[j])):
                ans.discard(unique[j]) 
    # print(ans)
    return len(ans)