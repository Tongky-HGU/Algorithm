from sys import stdin
import time
from functools import cmp_to_key

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

# def LCP():
#     global lcp, idx
#     k=0
#     for i in range(0,n):
#         if pos[i] == n-1 : continue;
#         j = sa[pos[i]+1]
#         # print(j)
#         # if j > n_1 : continue
#         while(1):
#             if i+k < n and j+k < n and s[i+k] == s[j+k]:
#                 k += 1
#             else:
#                 break
#         print(k)
#         if k > lcp:
#             lcp = k
#             idx = j
#         k = max(k-1,0)

# def LCP():
#     global lcp, idx
#     k=0
#     for i in range(n_1+1,n):
#         if n-i < lcp : break
#         if pos[i] == n-1 : continue
#         j = sa[pos[i]+1]
#         if j > n_1 : continue
#         while(1):
#             if i+k < n and j+k < n and s[i+k] == s[j+k]:
#                 k += 1
#             else:
#                 break
#         if k > lcp:
#             lcp = k
#             idx = j
#         k = max(k-1,0)
        

s1 = str(stdin.readline().rstrip())
s2 = str(stdin.readline().rstrip())

# s1 ='a'*100000
# s2 ='a'*100000


if len(s1) >= len(s2):
    s = s1 + '#' + s2
    n_1 = len(s1)
else:
    s = s2 + '#' + s1
    n_1 = len(s2)

# s = str(stdin.readline().rstrip())
# # # s= 'a'*100000
# n_1 = len(s)
# # # s= s+'#'+'a'*100000
# s = s +'#'+ str(stdin.readline().rstrip())

start = time.time()

n = len(s)

sa =[i for i in range(n)]
pos = [ord(s[i]) for i in range(n)]
lcp = [0]*n
idx = 0


d=1
while(1):
    # sa.sort(key=cmp_to_key(cmp))
    sa.sort(key=lambda x: (getGroup(x), getGroup(x + d)))
    #그룹 지정
    temp = [0]*(n)
    for i in range(n-1):
        temp[i+1] = temp[i]    
        if cmp(sa[i],sa[i+1]) < 0:
            temp[i+1] += 1

    for i in range(n):
        pos[sa[i]] = temp[i]

    if temp[n-1] == n-1:
        break

    d *= 2

LCP()

maxlcp = 0

print(lcp)

for i in range(len(lcp)):
    if  i > n_1 and lcp[i] > maxlcp :
        maxlcp = lcp[i]
        idx = sa[i]

print(maxlcp)

print(s[idx:idx+maxlcp])

print("time :", time.time() - start) 

