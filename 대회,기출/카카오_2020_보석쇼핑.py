import math

def solution(gems):
    cl=0
    cr=0
    
    gem_list = set(gems)
    gem_num = len(gem_list)
    
    gem_dict = zip(list(gem_list),[i for i in range(gem_num)])
    gem_dict = dict(gem_dict)
    # print(gem_dict)
    
    gem_list = [0 for _ in range(gem_num)]
    
    # print(gem_list)
    
    
    gems = [''] +gems
    N = len(gems)
    
    gem_cnt =0
    ans =[]
    
    min_len = math.inf
    
    while(1):
        if gem_cnt < gem_num:
            cr += 1
            
            if(cr == N):  #넘어가면 종료
                break
            
            if gem_list[gem_dict[gems[cr]]] == 0: #새로운 보석
                gem_cnt += 1

            gem_list[gem_dict[gems[cr]]] += 1     # 보석담기

        else:
            cl += 1
            
            gem_list[gem_dict[gems[cl]]] -= 1     # 보석버리기
            
            if gem_list[gem_dict[gems[cl]]] == 0: # 종류 중 하나 남은 보석 버리기
                gem_cnt -= 1
        
        
        if gem_cnt == gem_num and (cr-cl) < min_len:  # 최소거리
            min_len=  cr-cl
            ans = [cl+1,cr]
            
#         print(gem_list)
#         print(gem_cnt)        
            
    # print(ans)
        
    return ans