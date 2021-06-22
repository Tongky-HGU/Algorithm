function solution(A) {
    // 투포인터
    let cl = 0
    let cr = 0
    let now = A[0]
    let ans = A[0]

    while (cl < A.length) {
        if ((A[cl] < 0 && cl != cr) || cr == A.length - 1) {
            now -= A[cl]
            cl += 1
        } else {
            cr += 1
            now += A[cr]
        }
        ans = Math.max(ans, now)

    }

    return ans
}