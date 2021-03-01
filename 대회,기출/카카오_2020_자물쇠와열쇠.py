def solution(key, lock):
    N = len(key)
    M = len(lock)
    ans = False
    hole_num = 0
    # 자물쇠 영역
    lockfield = [[0 for _ in range(M+2*N-2)] for _ in range(M+2*N-2)]
    for i in range(M):
        for j in range(M):
            if lock[i][j]:
                lockfield[i+N-1][j+N-1] = 1
                hole_num +=1
    # for i in range(M+2*N-2):
        # print(lockfield[i])
        
    # 키 영역
    keyfield =[[[0 for _ in range(N)] for _ in range(N)] for _ in range(4)]
    keyfield[0] = key
    for i in range(1,4):
        keyfield[i] = list(zip(*keyfield[i-1]))
        keyfield[i].reverse()
    # print(keyfield[0]);
    # print(keyfield[1]);
    # print(keyfield[2]);
    # print(keyfield[3]);

    # validate
    for i in range(M+N-1):
        for j in range(M+N-1):
            # print(str(i)+ ","+str(j),end="")
            for k in range(4):
                cnt = 0
                # print("----------")
                # 키 삽입
                for q in range(N):
                    for l in range(N):
                        if keyfield[k][q][l] == 1:
                            lockfield[i+q][j+l] +=1
                # 비교    
                for q in range(M):
                    for l in range(M):
                        if lockfield[N+q-1][N+l-1] == 1:
                            cnt +=1
                if cnt == M*M :
                    return True
                # 키 제거
                for q in range(N):
                    for l in range(N):
                        if keyfield[k][q][l] == 1:
                            lockfield[i+q][j+l] -=1
    return False