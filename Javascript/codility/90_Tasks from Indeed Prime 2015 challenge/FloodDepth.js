function solution(A) {
    // 높이가 떨어지 때 계산
    let ans = 0
    let H = 0
    let L = 0
    for (let i = 0; i < A.length; i++) {
        if (A[i]>H){
            ans = Math.max(ans,H-L)
            H = A[i]
            L = A[i]
        }else if (A[i]<L){
            L = A[i]
        }else if (A[i]>L){
            ans = Math.max(ans,A[i]-L)
        }
        // console.log(H,L)
    }

    // console.log(ans)
    return ans
}