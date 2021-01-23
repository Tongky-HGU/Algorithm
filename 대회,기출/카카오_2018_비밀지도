def solution(n, arr1, arr2):
    ans = []
    
    for i in range(n):
        a = bin(arr1[i]|arr2[i])
        b = ''
        for _ in range(n + 2 - len(a)):
            b = b +' '
        for j in range(2,len(a)):
            if a[j] == '1':
                b = b+ '#'
            else:
                b = b+ ' '
                
        ans.append(b)
    print(ans) 
    return ans