# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
# 연습하려고 힙 정렬 써봣음

n = int(input())
ans=[]
for i in range(n):
    a = int(input())
    ans.append(a)

def heap_sort(a):
    def down_heap(a,left,right):
        temp = a[left] #루트
        parent = left
        while parent < (right+1) // 2:
            cl = parent*2+1
            cr = cl + 1
            child = cr if cr <= right and a[cr] > a[cl] else cl # 둘 중 큰 값
            # print(a[cr], a[cl])
            if temp >= a[child]:
                break
            a[parent] = a[child]
            parent = child
        a[parent] = temp 
    n = len(a)
    for i in range((n-1)//2,-1,-1):
        down_heap(a,i,n-1)
    for i in range(n-1,0,-1):
        a[0], a[i]  = a[i], a[0]
        down_heap(a,0,i-1)

heap_sort(ans)

for i in range(len(ans)):
    print(ans[i])