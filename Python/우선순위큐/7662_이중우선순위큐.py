import sys
import bisect
from collections import deque

test = int(sys.stdin.readline())

for _ in range(test):
    N = int(sys.stdin.readline())
    stack = deque()
    cnt = {}

    for i in range(N):
        order, num = sys.stdin.readline().split()
        num = int(num)
        if order == "I":
            if num in cnt: 
                cnt[num] += 1
            else:
                cnt[num] = 1
                bisect.insort_left(stack,num)
        else:
            if not stack: continue

            if num == 1:
                last = stack[-1]
                if cnt[last] > 1: 
                    cnt[last] -= 1
                else:
                    del cnt[last]
                    stack.pop()
            else:
                first = stack[0]
                if cnt[first] > 1: 
                    cnt[first] -= 1
                else:
                    del cnt[first]
                    stack.popleft()

    if not stack:
        print("EMPTY")
    else:
        print(stack[-1],stack[0])