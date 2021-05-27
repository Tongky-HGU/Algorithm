# 쿠키구입
def solution(cookie):
    ans = 0
    N = len(cookie)
    for i in range(N-1):
        cl, left = i, cookie[i]
        cr, right = i+1, cookie[i+1]
        # print('---')
        
        while(1):
            # print(cl,cr)
            if left == right:
                ans = max(ans,left)
                
            if left <= right and cl > 0:
                cl -= 1
                left += cookie[cl]
            elif left >= right and cr < N-1:
                cr += 1
                right += cookie[cr]
            else:
                break
    
    return ans