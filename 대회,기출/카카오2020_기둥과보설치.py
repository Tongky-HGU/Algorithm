#기둥과 보설치
import copy
def check(result):
    COL,ROW = 0, 1
    for x,y,a in result:
        if a == COL:
            if y != 0 and (x,y-1,COL) not in result and (x-1,y,ROW) not in result and (x,y,ROW) not in result:
                return True
        else:
            if(x,y-1,COL) not in result and (x+1,y-1,COL) not in result and not ((x-1,y,ROW) in result and (x+1,y,ROW) in result):
                return True
    return False

def solution(n, build_frame):
    result = set()

    for x,y,a,build in build_frame:
        item = (x,y,a)
        if build:
            result.add(item)
            if check(result):
                result.remove(item)
        elif item in result:
            result.remove(item)
            if check(result):
                result.add(item)
    ans = map(list,result)
    ans = sorted(ans)
    return ans

