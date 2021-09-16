def solution(weights, head2head):
    N = len(weights)
    ans = [i for i in range(N)]

    def getWinRate(x):
        game = len(list(filter(lambda x: x=='W' or x=='L',head2head[x])))
        win = len(list(filter(lambda x: x=='W',head2head[x])))
        if game == 0 : return 0
        return win/game

    def getWinHeavy(me):
        A = [i for i in range(N)]
        myWeight = weights[me]
        win = filter(lambda x: head2head[me][x]=='W',A)
        heavyWin = len(list(filter(lambda x: weights[x]>myWeight,win)))
        return heavyWin

    ans.sort(key=lambda x:(-getWinRate(x),-getWinHeavy(x), -weights[x], x))
    
    return list(map(lambda x: x+1, ans))

print(solution(	[60, 70, 65], ["NNN", "NNN", "NNN"]))




