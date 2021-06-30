#기지국 설치
import math

def solution(n, stations, w):
    ans = 0
    cur = 1
    for station in stations:
        l = station - w
        r = station + w

        if l <= cur:
            cur = r + 1
            continue

        ans += math.ceil((l - cur)/(2*w+1))
        cur = r + 1
        print(cur,ans)

    if cur <= n+1:
        ans += math.ceil((n+1 - cur)/(2*w+1))

    return  ans

