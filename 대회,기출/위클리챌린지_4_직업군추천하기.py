def solution(table, languages, preference):
    ans = ''
    maxScore = 0
    score = {}
    for s in table:
        A = s.split()
        company = A[0]
        score[company] = {}
        for i,language in enumerate(A[1:]):
            score[company][language] = 5-i
    print(score)
    for company in score:
        cnt = 0
        for lan,pref in zip(languages,preference):
            if lan in score[company]:
                cnt += (pref * score[company][lan])
        if cnt > maxScore:
            ans = company
            maxScore = cnt
    print(ans)
    return ans

solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]	,["PYTHON", "C++", "SQL"],	[7, 5, 5])