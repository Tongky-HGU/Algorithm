# 가르침
import sys
N, K = map(int,sys.stdin.readline().split())

A = ['b','d','e','f','g','h','j','k','l','m','o','p','q','r','s','u','v','w','x','y','z']
B = ['a','c','i','n','t']

ans = 0

def dfs(i,start,depth):
    global ans
    if depth == K-5:
        i |= need
        cnt = 0
        for word in words:
            if ( word & i == word):
                cnt+=1
        ans = max(ans,cnt)
        return

    for j in range(start,len(A),1):
        num = i | (1<< ord(A[j])-ord('a'))
        dfs(num,j+1,depth+1)
    return

if (K < 5):
    print(0)
else:
    #필수 단어 bitmasking
    need = 0
    for i in range(5):  
        need |= (1<< ord(B[i])-ord('a'))

    # string 마다 필요한 철자
    words = [0] * N
    for i in range(N):
        string = sys.stdin.readline().rstrip()
        for char in string:
            words[i] |= (1<< ord(char) - ord('a'))

    # print(need)
    # print(words)

    # dfs로 조합 완전탐색   
    dfs(0,0,0)

    print(ans)
