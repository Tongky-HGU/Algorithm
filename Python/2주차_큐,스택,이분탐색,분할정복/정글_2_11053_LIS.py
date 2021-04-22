# 가장 긴 증가하는 부분수열 LIS
import sys

n = int(sys.stdin.readline())
a = [0] + list(map(int,sys.stdin.readline().split()))

def getLIS(a):
    lis = [1]*(n+1)
    temp_lis = [0]
    temp_idx = [0]
    for i in range(0,n+1):
        cl = 0
        cr = len(temp_idx)-1
        mid = 0
        while(cl <= cr):
            mid = (cl+cr)//2
            if temp_idx[mid] > a[i]:
                cr = mid-1
            elif temp_idx[mid] < a[i]:
                cl = mid+1
            else:
                break
        # print(str(i)+"------")    
        # print("a 값:" + str(a[i]))
        # print("temp 값:" +str(temp_idx[mid]))
        if temp_idx[mid] == a[i]:
            lis[i] = temp_lis[mid]
        elif a[i]> temp_idx[mid] :
            if (mid < len(temp_idx)-1):
                lis[i] = temp_lis[mid]+1
                temp_idx[mid+1] = a[i] 
            else:
                lis[i] = temp_lis[mid]+1
                temp_lis.append(lis[i])
                temp_idx.append(a[i])
        else:
            lis[i] = temp_lis[mid]
            temp_idx[mid] = a[i]

        # print(a)
        # print(lis)
        # print(temp_lis)
        # print(temp_idx)

    return lis
              
        
print(max(getLIS(a)))
