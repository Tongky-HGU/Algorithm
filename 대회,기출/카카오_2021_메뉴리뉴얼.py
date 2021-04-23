# 메뉴리뉴얼
from itertools import combinations
from collections import Counter


def solution(orders, course):
    ans = []
    for L in course:
        temp = []
        for order in orders:
            temp += combinations(sorted(order),L)
        
        count = Counter(temp)
        if len(count) == 0 or max(count.values()) == 1: continue
        
        ans += [''.join(f) for f in count if count[f] == max(count.values())]
                
    return sorted(ans)