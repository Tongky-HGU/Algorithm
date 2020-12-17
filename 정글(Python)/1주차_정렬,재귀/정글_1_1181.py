# 알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.
import sys
n = int(sys.stdin.readline())
a = []
for i in range(n): a.append(str(sys.stdin.readline().rstrip()))

def compare_dict(a,b):
    if(a==b):
        return a
    else:
        for i in range(len(a)):
            if ord(a[i]) == ord(b[i]):
                continue
            elif ord(a[i]) < ord(b[i]):
                return a
            else: 
                return b


def heap_sort(a):
    def down_heap(a,left,right):
        temp = a[left]
        parent = left
        while parent < (right+1)//2:
            cl = parent*2+1
            cr = cl + 1
            if cr <= right and len(a[cr]) >len(a[cl]):
                child = cr 
            elif cr <= right and len(a[cr]) == len(a[cl]):
                if a[cr] != compare_dict(a[cr],a[cl]):
                    child = cr
                else:
                    child = cl
            else: child = cl

            if len(temp) > len(a[child]):
                break
            elif len(temp) == len(a[child]):
                if temp != compare_dict(temp,a[child]):
                    break
            a[parent] = a[child]
            parent = child
        a[parent] = temp
    for i in range((n-1)//2,-1,-1):
        down_heap(a,i,n-1)
    for i in range(n-1,0,-1):
        a[0],a[i] = a[i],a[0]
        down_heap(a,0,i-1)

heap_sort(a)

a.append([])
for i in range(n):
    if a[i] == a[i+1]:
        continue
    else:
        print(a[i])