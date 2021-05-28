#가장큰수 
def solution(numbers):
    ans = ''
    numbers = list(map(str,numbers))
    numbers.sort(key = lambda x : x*2, reverse=True)
    return str(int(''.join(numbers)))