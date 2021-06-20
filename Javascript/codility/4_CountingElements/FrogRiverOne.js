function solution(X, A) {
    // A 에 대해 for 문 돌면서 X보다 작고 set에 없다면
    // cnt가 X가 되면 idx 리턴
    let leaves = new Set()
    let cnt = 0
    for (let i = 0; i < A.length; i++) {
        if (A[i] <= X && !leaves.has(A[i])) {
            leaves.add(A[i])
            cnt += 1
        }
        if (cnt == X){
            return i
        }
    }
    return -1
}