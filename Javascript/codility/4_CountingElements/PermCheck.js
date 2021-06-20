function solution(A) {
    // set에 집어 넣고 1부터 확인
    check = new Set(A)
    for (let i = 1; i < A.length + 1; i++) {
        if (!check.has(i)) {
            return 0
        }
    }
    return 1
}