# 입력으로 종이의 가로 세로 길이, 그리고 잘라야할 점선들이 주어질 때, 가장 큰 종이 조각의 넓이가 몇 ㎠인지를 구하는 프로그램을 작성하시오. 

w, h = map(int,input().split())
n = int(input())

w_point = [0]
h_point = [0]
for i in range(n):
    direction ,point = map(int,input().split());
    if(direction==0):
        h_point.append(point)
    else:
        w_point.append(point)
h_point.append(h)
w_point.append(w)

h_point = sorted(h_point)
w_point = sorted(w_point)

h_dist = []
w_dist = []
for i in range(len(h_point)-1):
    h_dist.append(abs(h_point[i]-h_point[i+1]))

for i in range(len(w_point)-1):
    w_dist.append(abs(w_point[i]-w_point[i+1]))

print(max(w_dist)*max(h_dist))
    





    
