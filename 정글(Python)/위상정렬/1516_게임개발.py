#게임개발
import sys,heapq
N = int(sys.stdin.readline())
time = [ 0 for _ in range(N+1)]
degree = [0 for _ in range(N+1)]
link = [[] for _ in range(N+1)]

for i in range(1,N+1):
    a = list(map(int,sys.stdin.readline().split()))
    time[i] = a[0]
    j=1
    while(a[j]!=-1):
        degree[i]+=1
        link[a[j]].append(i)
        j+=1

# print(time)
# print(degree)
# print(link)

queue= []
for i in range(1,N+1):
    if(degree[i]==0):
        heapq.heappush(queue,[time[i],i])

while(queue):
    t, index = heapq.heappop(queue)
    degree[index] = -1
    time[index] = t
    for i in link[index]:
        degree[i] -= 1
        if(degree[i]==0):
            heapq.heappush(queue,[time[i]+t,i])

for i in range(1,N+1):
    print(time[i])

    