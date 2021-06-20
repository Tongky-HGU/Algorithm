function solution(N) {
    ans = 0
    A = N.toString(2).split('')
    cnt = 0
    for (let i = 0; i < A.length; i++) {
        if (A[i] == 0) {
            cnt += 1
        }
        else {
            ans = Math.max(ans,cnt)
            cnt = 0
        }
    }
    return ans
}