#8진수 10진수 16진수
import sys
A = str(sys.stdin.readline().rstrip())

def change():
    if A[0]=='0' :
        if A[1]=='x':
            print(int(A,16))
            return
        print(int(A,8))
        return
    print(int(A))
    return

change()