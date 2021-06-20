function solution(A) {
    // slice로 나누고 for문 돌면서 하나씩 옮겨준다.
    let L = A[0]
    let R = A.slice(1).reduce((sum,a)=>{
        return sum + a
    })
    let ans = Math.abs(L-R)
    for(let i = 1; i < A.length-1; i++){
        L += A[i]
        R -= A[i]
        ans = Math.min(ans,Math.abs(L-R))
    }
    return ans
}