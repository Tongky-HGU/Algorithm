import sys

test = int(sys.stdin.readline())

for _ in range(test):
  ans = 1
  N = int(sys.stdin.readline())
  category = {}

  for _ in range(N):
    A, item = sys.stdin.readline().rstrip().split()
    if item in category:
      category[item].append(A)
    else:
      category[item] = [A]

  for item in category.keys():
    ans = ans * (len(category[item]) + 1)

  print(ans - 1)