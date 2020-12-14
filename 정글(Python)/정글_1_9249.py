# 문자열 가 문자열 의 부분 문자열이 되려면, 를 만족하는 가 있어야 한다.

# 두 문자열 와 가 주어졌을 때, 두 문자열의 공통 부분 문자열의 최대 길이와 그 부분 문자열을 구하는 프로그램을 작성하시오.

a = str(input())
b = str(input())
for i in range(len(b)):
    count = a.count(b[i:])
    if count >= 1:
        ans = (b[i:])
        break
print(len(ans))
print(ans)

    


