import re
from itertools import permutations

def calculate(a,b,equation):
    if equation == '+':
        return a+b
    elif equation == '-':
        return a-b
    else:
        return a*b

def solution(expression):
    equation = re.findall('[*+-]',expression)
    number = list(map(int,re.split('[*+-]',expression)))

    original = [number[0]]
    for i in range(len(equation)):
        original.append(equation[i])
        original.append(number[i+1])
        
    ans = 0
    combis = permutations(set(equation),len(set(equation)))
    for combi in combis:
        level = 0
        stack = original
        while(1):
            temp = [stack[0]]
            for i in range(1,len(stack),2):
                if stack[i] == combi[level]:
                    num = temp.pop()
                    temp.append(calculate(num,stack[i+1],combi[level]))
                else:
                    temp.append(stack[i])
                    temp.append(stack[i+1])

            if len(temp) == 1:
                ans = max(ans,abs(temp[0]))
                break
            else:
                level +=1
                stack = temp
    return ans