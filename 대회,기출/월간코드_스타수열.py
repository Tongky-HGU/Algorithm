# 스타수열
from collections import Counter

def solution(a):
    ans = 0
    count = Counter(a)
    for x in count:
        if count[x] * 2 <= ans : continue
        idx = 1
        cnt = 0
        while idx < len(a):
            if (a[idx] != x and a[idx-1] != x) or a[idx - 1] == a[idx]:
                idx += 1
                continue
            idx += 2
            cnt += 2
        
        ans = max(ans,cnt)

    return ans
print(solution([0,3,3,0,7,2,0,2,2,0]))