#01타일
import sys
def sol():
	if N == 1:
	   print(1)
	   return
	d = [0]*(N+1)
	d[1],d[2] = 1,2
	for i in range(3,N+1):
		d[i] = (d[i-1] + d[i-2]) %15746
	print(d[N])

N = int(sys.stdin.readline())

sol()
