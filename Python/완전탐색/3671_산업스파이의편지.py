import sys
from itertools import permutations

def prior(num):
    if num == 0 or num == 1 : return False
    for i in range(2,int(num**(1/2))+1):
        if num % i == 0: return False
    return True


N = int(sys.stdin.readline())

for _ in range(N):
    A = sys.stdin.readline().rstrip()
    cnt = set()
    for i in range(1,len(A)+1):
        combis = permutations(A,i)
        for combi in combis:
            num = int(''.join(combi))
            if(prior(num)):
                cnt.add(num)
    print(len(cnt))
