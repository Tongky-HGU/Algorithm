from itertools import product

def solution(word):
    A = 'AEIOU'
    L = []
    for i in range(1,6):
        combis = product(A, repeat=i)
        for combi in combis:
            L.append(''.join(combi))
    L.sort()
    ans = L.index(word)
    return ans

print(solution("AAAAE"))
