def solution(scores):
    ans = ''
    
    for i,score in enumerate(zip(*scores)):
        average = 0
        if score.count(score[i]) == 1 and (score[i] == max(score) or score[i] == min(score)):
            average = (sum(score) - score[i])/(len(score)-1)
        else:
            average = sum(score)/len(score)
            
        if average >= 90:
            ans += "A"
        elif average >= 80:
            ans += "B"
        elif average >= 70:
            ans += "C"
        elif average >= 50:
            ans += "D"
        else:
            ans += "F"
    return ans