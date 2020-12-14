# (1)과 (2)위치에 들어갈 세 자리 자연수가 주어질 때 (3), (4), (5), (6)위치에 들어갈 값을 구하는 프로그램을 작성하시오.

import sys

# a = int(sys.stdin.readline().rstrip())
# b = int(sys.stdin.readline().rstrip())
a = int(input())
b = int(input())
ans =a*b

print(a*(b%10))
b = int(b/10)
print(a*(b%10))
b = int(b/10)
print(a*(b%10))

print(ans)