# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
# 지수 정렬로 풀어봤는데 안되서 진짜 배열에 저장 1도 안하고 하게끔 만들어야됨....
import sys
n = int(sys.stdin.readline())
f = [0] * 10001
for i in range(n):
    f[int(sys.stdin.readline())] += 1
for i in range(1,10001):
    for _ in range(f[i]):
        print(i)