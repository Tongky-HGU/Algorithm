# 대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.
n = int(input())
for i in range(n):
    a = list(map(int,input().split()))
    avg =sum(a[1:])/(len(a)-1)
    count = 0
    for j in range(a[0]):
        if a[j+1] > avg:
            count +=1
    print("{:.3f}%".format(count/a[0]*100))

    
        