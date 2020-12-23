import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())
a = deque(i+1 for i in range(n))
while(len(a)>1):
    a.popleft()
    a.append(a[0])
    a.popleft()
print(*a)

