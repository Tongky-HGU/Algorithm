#숫자문자열과 영단어

def solution(s):
    ans = []
    num = {'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
    jump = 0
    for i in range(len(s)):
        if jump > 0:
            jump -= 1
            continue
        if s[i].isdigit():
            ans.append(s[i])
        else:
            if s[i:i+3] in num:
                ans.append(num[s[i:i+3]])
                jump = 2
                continue
            if s[i:i+4] in num:
                ans.append(num[s[i:i+4]])
                jump = 3
                continue
            if s[i:i+5] in num:
                ans.append(num[s[i:i+5]])
                jump = 4
                continue
    return int(''.join(ans))

print(solution('one4seveneight'))