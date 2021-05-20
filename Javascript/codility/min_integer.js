function solution(A) {
    let ans = 1

    A.sort((a,b)=> a-b) // 오름차순
    for (let i = 0; i < A.length; i++) {
        if (A[i] < ans) {
            continue
        } else if (A[i] == ans) {
            ans += 1
        } else {
            break
        }
    }
    return ans
}