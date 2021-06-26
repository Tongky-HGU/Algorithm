import re 
import copy
# 매칭점수
def solution(word, pages):
    ans = 0
    maxScore = 0
    basicScores = {}
    pageScores = {}
    linked = {}

    word = word.lower()

    for page in pages:
        wordCnt = 0
        linkCnt = 0
        
        page = page.lower()
        name = re.search(r'<meta[^>]*content="https://([\S]*)"/>',page).group(1)

        #word counting
        for string in re.findall(r'[a-zA-Z]+',page):
            # print(string)
            if string == word:
                wordCnt +=1

        #link counting
        for string in re.findall(r'<a href="https://[\S]*">',page):
            link = re.search(r'"https://([\S]*)"',string).group(1)
            linkCnt +=1
            if link in linked:
                linked[link].append(name)
            else:
                linked[link] = [name]

        # print(wordCnt,linkCnt)
        basicScores[name] = wordCnt
        pageScores[name] = wordCnt / linkCnt if linkCnt != 0 else 0

    print(pageScores)
    print(linked)

    # score
    totalScore = copy.deepcopy(basicScores)
    for key,link in linked.items():
        score = 0
        if key in totalScore:
            for l in link:
                if l in pageScores:
                    score += pageScores[l]
            
            totalScore[key] += score

    print(totalScore)


    for idx,key in enumerate(totalScore):
        if totalScore[key] > maxScore :
            ans = idx
            maxScore = totalScore[key]

    return ans

print(solution("blind",["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]))