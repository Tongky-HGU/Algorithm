import sys 
number, multiple, divide = list(map(int,sys.stdin.readline().split()))

def pow(a,n):
    if n == 0:
        return 1
    elif n == 1:
        return a
    elif n % 2 > 0:
        return pow(a,n-1)*a
    else:
        half = pow(a,n/2)
        half = half % divide
        return (half*half) % divide

print(int(pow(number,multiple)%divide))

