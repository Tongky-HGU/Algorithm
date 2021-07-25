# 통계학 counting sort
import sys
from collections import Counter

def roundUp(number):
    if number >=0 :
        if number - int(number) >= 0.5: 
            return int(number)+1
        else: 
            return int(number)
    else:
        number = -1 * number 
        if number - int(number) >= 0.5: 
            return -1 * (int(number)+1)
        else: 
            return -1 * (int(number))


N = int(sys.stdin.readline())
A = []

for _ in range(N):
    A.append(int(sys.stdin.readline()))

count = Counter(A)

MAX = count.most_common()[0][1]
B = []

for key,cnt in count.items():
    if cnt == MAX:
        B.append(key)

A.sort()
B.sort()

print(roundUp(sum(A)/N))
print(A[N//2])
if len(B) == 1:
    print(B[0])
else:
    print(B[1])
print(A[-1]-A[0])

