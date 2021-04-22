from sys import stdin
import time
from functools import cmp_to_key

def compare_sa():
    for i in range(n-1):
        for j in range(0,n-i-1):
            swap = False
            if pos[sa[j]] != pos[sa[j+1]]:
                if pos[sa[j]] > pos[sa[j+1]]:
                        swap =True
            else:
                if sa[j]+d <n and sa[j+1]+d <n : #범위 안이라면
                    if pos[sa[j]+d] > pos[sa[j+1]+d]:
                        swap =True
                else:
                    if sa[j] < sa[j+1]:
                        swap =True
            if swap:
                sa[j],sa[j+1] = sa[j+1],sa[j]

def cmp(i,j):
    if pos[i] != pos[j]:
        return pos[i] - pos[j]
    i += d
    j += d
    if i <n and j <n :
        return pos[i] - pos[j]
    else:
        return j - i

def getGroup(x):
        if x < n:
            return pos[x]
        else:
            return -1


def LCP():
    k=0
    for i in range(0,n):
        if pos[i] == n-1 : continue;
        j = sa[pos[i]+1]
        while(1):
            if i+k < n and j+k < n and s[i+k] == s[j+k]:
                k += 1
            else:
                break
        lcp[pos[i]+1]=k
        k = max(k-1,0)
            
        
s = str(stdin.readline().rstrip())
# s = 'a'*200000

# start = time.time()

n = len(s)
sa =[i for i in range(n)]
pos = [ord(s[i]) for i in range(n)]
lcp = ['x']*n

d=1
while(1):
    # compare_sa()
    sa.sort(key=lambda x: (getGroup(x), getGroup(x + d)))
    # sa.sort(key=cmp_to_key(cmp))
    #그룹 지정
    temp = [0]*n
    for i in range(n-1):
        if cmp(sa[i],sa[i+1]) < 0:
            temp[i+1] = temp[i] + 1
        else:
            temp[i+1] = temp[i]

    for i in range(n):
        pos[sa[i]] = temp[i]

    if temp[n-1] == n-1:
        break
    d = 2*d

LCP()

for i in range(n):
    sa[i] += 1

print(*sa)
print(*lcp)

# for i in range(n):
#     print(sa[i], end=' ')
# print()

# for i in range(n):
#     print(lcp[i], end=' ')
# print()

# print("time :", time.time() - start) 
