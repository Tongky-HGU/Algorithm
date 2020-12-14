import sys
a,b,c,d = map(int,sys.stdin.readline().rstrip().split())

# a,b,c,d = map(int,input().split())
print(min(abs(a-c),abs(b-d)))