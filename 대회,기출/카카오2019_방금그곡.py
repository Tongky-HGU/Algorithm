#방금그곡
def timeToHour(time):
    ret = time.split(':')
    return int(ret[0])*60 + int(ret[1])

def getPlayingTime(start,end):
    return timeToHour(end) - timeToHour(start) 

def getCode(string):
    code = []
    for char in string:
        if char == '#':
            temp = code.pop()
            code.append(temp+'#')
        else:
            code.append(char)
    return code
    
def solution(m, musicinfos):
    candidates = []
    m = getCode(m)
    M = ''.join(m)
    for idx,musicinfo in enumerate(musicinfos):
        start,end,title,codeString = musicinfo.split(',')
        code = getCode(codeString)
        playingTime = getPlayingTime(start,end)

        while(len(code) < playingTime):
            code = code + code[0:playingTime-len(code)]

        if len(code) > playingTime:
            code = code[:playingTime]

        for i in range(0,len(code)-len(m)+1):
            if M == ''.join(code[i:i+len(m)]):
                candidates.append([playingTime,-idx,title])
                break
        # print(code)

    # print(candidates)
    if candidates:
        candidates.sort(reverse=True)
        return candidates[0][2]
    return "(None)"
