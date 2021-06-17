#자물쇠와 열쇠
import copy

def createLockPad(lock,key):
    N = len(lock)
    M = len(key)
    new = [[0 for _ in range(N+2*M-2)] for _ in range(N+2*M-2)]
    for r in range(N):
        for c in range(N):
            if lock[r][c] == 1:
                new[r+M-1][c+M-1] = 1
    return new

def rotate(key):
    new = [[0 for _ in range(len(key))] for _ in range(len(key))]
    for r in range(len(key)):
        for c in range(len(key)):
            if key[r][c] == 1:
                new[c][len(key)-r-1] = 1
    return new

def check(keyPad,N,M):
    for i in range(M-1,N+M-1):
        for j in range(M-1,N+M-1):
            if keyPad[i][j] != 1:
                return False
    return True

def solution(key, lock):
    ans = False
    N = len(lock)
    M = len(key)

    lockPad = createLockPad(lock,key)

    for _ in range(4):    
        key = rotate(key)
        for i in range(len(lockPad)-M+1):
            for j in range(len(lockPad)-M+1):
                keyPad = copy.deepcopy(lockPad)
                for x in range(M):
                    for y in range(M):
                        keyPad[i+x][j+y] += key[x][y]
                if(check(keyPad,N,M)):
                    return True

    return ans
