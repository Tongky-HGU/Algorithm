import sys
N = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())

cl = 0
cr = max(A)
while cl<=cr:
  mid = (cl+cr)//2
  spend = 0
  
  for i in A:
    if i<mid:
      spend += i
    else:
      spend += mid

  if spend <= M:
    cl = mid+1
  else:
    cr = mid-1

print(cr)
  