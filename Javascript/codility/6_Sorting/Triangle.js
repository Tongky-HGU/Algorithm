function solution(A) {
    // sorting 해놓고 작은 거 더한 값이 1인지 확인
    if (A.length < 3) return 0
    A.sort((a, b) => { return a - b })
    for (let i = 0; i < A.length - 2; i++) {
        if (A[i] + A[i + 1] > A[i + 2]) {
            return 1
        }
    }
    return 0
}