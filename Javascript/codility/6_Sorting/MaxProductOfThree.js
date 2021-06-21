function solution(A) {
    A.sort((a,b)=>{return a-b})
    // 앞에서 3개
    let i = A.length -1
    let ans = A[i]*A[i-1]*A[i-2]

    // 음수가 있을 경우
    ans = Math.max(ans,A[i]*A[0]*A[1])
    return ans
}